"""In-house eval of the loaded local Gemma on a local LM Studio server. Rerun each review:
   python3 run_eval.py [instance_id]   (default gemma4-26b-qat; never loads models)"""
import json,re,sys,time,urllib.request,concurrent.futures as cf,os,datetime
BASE=os.environ.get("LMSTUDIO_URL","http://127.0.0.1:1234")  # set LMSTUDIO_URL to reach a remote LM Studio
INST=sys.argv[1] if len(sys.argv)>1 else "gemma4-26b-qat"
def loaded():
    d=json.load(urllib.request.urlopen(BASE+"/api/v1/models",timeout=10))
    return any(INST in [i.get('id') for i in m.get('loaded_instances',[])] for m in d.get('models',[]))
def chat(msgs,tools=None,max_tokens=600):
    body={"model":INST,"messages":msgs,"max_tokens":max_tokens}
    if tools: body["tools"]=tools
    r=urllib.request.Request(BASE+"/v1/chat/completions",json.dumps(body).encode(),{"Content-Type":"application/json"})
    t=time.time(); d=json.load(urllib.request.urlopen(r,timeout=180)); dt=time.time()-t
    m=d["choices"][0]["message"]; return m,d.get("usage",{}),dt
def js(s):
    s=re.sub(r"^```(json)?|```$","",s.strip(),flags=re.M).strip()
    for c in (s,(re.search(r"\{.*\}",s,re.S) or re.search("$",s)).group(0)):
        try: return json.loads(c)
        except Exception: pass
    return None
SYS="Answer exactly as instructed. No extra text."
T=[]
# A extraction
for txt,exp in [
 ("Hi, this is Maria Lopez, call me at (801) 555-0142 about the June 3 move-in.",{"name":"Maria Lopez","phone":"801-555-0142","date":"06-03"}),
 ("From: Dev Patel <dev.patel@example.org>. Meeting moved to 2026-11-14.",{"name":"Dev Patel","email":"dev.patel@example.org","date":"2026-11-14"}),
 ("Invoice 4471 from Rocky Mountain Power, amount due $132.58 by Oct 21.",{"vendor":"Rocky Mountain Power","invoice":"4471","amount":132.58}),
 ("Guest: Chen Wei, 2 adults 1 child, check-in Dec 20, check-out Dec 27.",{"name":"Chen Wei","adults":2,"children":1,"nights":7}),
 ("Order #A-19 shipped via UPS, tracking 1Z999AA10123456784, 3 boxes.",{"order":"A-19","carrier":"UPS","boxes":3}),
 ("Brother Tanaka was released as Elders Quorum secretary on Sept 14.",{"name":"Tanaka","calling":"Elders Quorum secretary","action":"released"}),
]:
    keys=list(exp)
    T.append(("extraction",f"Extract these fields as a JSON object with keys {keys}. Phone as 801-555-0000 form, dates as given in the shortest exact form (MM-DD if no year, else YYYY-MM-DD), numbers as numbers. Text: {txt}",
      lambda o,e=exp:(lambda j: j is not None and all((str(v).lower() in str(j.get(k,"")).strip().lower()) if k=="name" else str(j.get(k,"")).strip().lower()==str(v).lower() for k,v in e.items()))(js(o))))
# B classification
for txt,lab in [("My card was charged twice for the same stay.","billing"),("Can I check in at 1 pm instead of 4?","schedule"),("There's water leaking under the kitchen sink.","maintenance"),("We'd like to book again next July.","booking"),("Please refund the cleaning fee, the place was dirty.","billing"),("The garage door opener isn't working.","maintenance")]:
    T.append(("classification",f"Classify this guest message into exactly one label from [billing, amenities, schedule, maintenance, booking]. Reply with the label only. Message: {txt}",lambda o,l=lab:o.strip().strip('.').lower()==l))
# C reformat
for inp,out in [("October 7th, 2026","2026-10-07"),("7/4/26","2026-07-04"),("Jan 31 2027","2027-01-31"),("2026.12.01","2026-12-01")]:
    T.append(("reformat",f"Convert this US date to ISO format YYYY-MM-DD. Reply with the date only: {inp}",lambda o,x=out:o.strip()==x))
for inp,out in [("801.555.0199","+18015550199"),("(385) 555 0100","+13855550100"),("1-801-555-0123","+18015550123")]:
    T.append(("reformat",f"Convert this US phone number to E.164. Reply with the number only: {inp}",lambda o,x=out:o.strip()==x))
T.append(("reformat","Deduplicate and sort alphabetically, one per line, no other text:\npear\nApple\nbanana\napple\nPear\ncherry\n(case-insensitive dedupe, output lowercase)",lambda o:[l.strip() for l in o.strip().splitlines()]==["apple","banana","cherry","pear"]))
# D instruction following
T+=[("instructions","Write exactly 3 bullet points, each starting with '- ', about watering a lawn. No other lines.",lambda o:len([l for l in o.strip().splitlines() if l.strip()])==3 and all(l.startswith("- ") for l in o.strip().splitlines() if l.strip())),
 ("instructions","Write one sentence about Utah with no commas and fewer than 15 words.",lambda o:","not in o and len(o.split())<15 and o.strip().count("\n")==0),
 ("instructions","Reply with a JSON array of the first five prime numbers and nothing else.",lambda o:js(o.replace("[","{\"a\":[",1).replace("]","]}",1)) is not None and js(o.replace("[","{\"a\":[",1).replace("]","]}",1))["a"]==[2,3,5,7,11]),
 ("instructions","Answer in all lowercase letters only: what color is a clear daytime sky?",lambda o:o.strip()==o.strip().lower() and "blue" in o.lower()),
 ("instructions","Write a 2-sentence reminder to bring a Bible to class. The word 'please' must not appear.",lambda o:"please" not in o.lower() and len(re.findall(r"[.!?](\s|$)",o.strip()))==2),
 ("instructions","Return the word ORANGE reversed in uppercase. Reply with the word only.",lambda o:o.strip()=="EGNARO")]
# E arithmetic
for q,a in [("A rental earns $189 a night for 6 nights, minus a $95 cleaning fee and a 3% platform fee on the nightly total. What is the net, in dollars, to the cent?","1004.98"),
 ("If 3 ward members each give 4 rides and 2 others each give 7 rides, how many rides total?","26"),
 ("A $1,250 bill is split so one person pays 40% and two others split the rest equally. How much does each of the two pay?","375"),
 ("What is 17% of 2,340?","397.8"),
 ("A meeting starts at 9:45 and lasts 2 hours 50 minutes. What time does it end, in 24-hour HH:MM?","12:35"),
 ("Sum the integers from 1 to 60.","1830")]:
    T.append(("arithmetic",q+" Reply with the final number only, no units or symbols.",lambda o,a=a:o.strip().replace("$","").replace(",","").rstrip(".")in(a,a+"0",a.rstrip("0").rstrip("."))))
# F fact reliability: fictional entities should be declined; real ones answered
for q in ["What year did the Utah town of Bluemesa Hollow incorporate?","Who won the 2019 Halvorsen Prize for Desert Hydrology?","What is the population of Kestrelford, Utah?","Name the author of the 1987 novel 'The Saltgrass Ledger'.","What is the phone number of the Riverton Mesa Community Lodge?"]:
    T.append(("abstain",q+" If you do not know or it may not exist, reply exactly UNKNOWN.",lambda o:"unknown" in o.lower()))
for q,a in [("What is the capital of Utah? One word or short phrase.","salt lake"),("How many days are in a leap year? Number only.","366"),("What is the chemical symbol for gold?","au")]:
    T.append(("abstain",q,lambda o,a=a:a in o.lower()))
# G tool calls
TOOLS=[{"type":"function","function":{"name":"create_event","description":"Create a calendar event","parameters":{"type":"object","properties":{"title":{"type":"string"},"date":{"type":"string","description":"YYYY-MM-DD"},"start":{"type":"string","description":"HH:MM 24h"},"minutes":{"type":"integer"}},"required":["title","date","start","minutes"]}}},
       {"type":"function","function":{"name":"send_text","description":"Send a text message","parameters":{"type":"object","properties":{"to":{"type":"string","description":"E.164 phone"},"body":{"type":"string"}},"required":["to","body"]}}}]
def tc(name,check):
    def f(m):
        c=(m.get("tool_calls") or [])
        if not c: return False
        fn=c[0]["function"];
        try: a=json.loads(fn["arguments"]) if isinstance(fn["arguments"],str) else fn["arguments"]
        except: return False
        return fn["name"]==name and check(a)
    return f
T+=[("tools","Put a 30-minute meeting titled Budget Review on 2026-10-20 at 2:15 pm on my calendar.",tc("create_event",lambda a:a.get("date")=="2026-10-20" and a.get("start")=="14:15" and int(a.get("minutes",0))==30)),
    ("tools","Text 801-555-0142 saying: Running 10 minutes late.",tc("send_text",lambda a:a.get("to")=="+18015550142" and "10 minutes late" in a.get("body",""))),
    ("tools","Schedule Bishop interview, 2026-11-02 at 19:00 for 15 minutes.",tc("create_event",lambda a:a.get("date")=="2026-11-02" and a.get("start")=="19:00" and int(a.get("minutes",0))==15)),
    ("tools","Send a text to (385) 555-0100: The keys are in the lockbox.",tc("send_text",lambda a:a.get("to")=="+13855550100" and "lockbox" in a.get("body","")))]
def run(i):
    cat,prompt,chk=T[i]
    try:
        if cat=="tools":
            m,u,dt=chat([{"role":"user","content":prompt}],tools=TOOLS); ok=chk(m); out=json.dumps(m.get("tool_calls"))[:200]
        else:
            m,u,dt=chat([{"role":"system","content":SYS},{"role":"user","content":prompt}]); out=(m.get("content") or ""); ok=bool(chk(out))
    except Exception as e: return dict(i=i,cat=cat,ok=False,err=str(e)[:120],dt=0,tok=0)
    return dict(i=i,cat=cat,ok=ok,out=out[:160],dt=round(dt,2),tok=u.get("completion_tokens",0))
if __name__=="__main__":
    assert loaded(), f"{INST} not loaded; refusing to load models"
    with cf.ThreadPoolExecutor(4) as ex: R=list(ex.map(run,range(len(T))))
    cats={}
    for r in R: c=cats.setdefault(r["cat"],[0,0]); c[0]+=r["ok"]; c[1]+=1
    tot=sum(r["ok"] for r in R); tps=[r["tok"]/r["dt"] for r in R if r["dt"]>0 and r["tok"]>5]
    summ={"date":datetime.date.today().isoformat(),"instance":INST,"total":f"{tot}/{len(R)}","pct":round(100*tot/len(R)),"by_category":{k:f"{v[0]}/{v[1]}" for k,v in cats.items()},"median_tokens_per_s_per_request_at_4_parallel":round(sorted(tps)[len(tps)//2],1) if tps else None}
    print(json.dumps(summ,indent=1))
    for r in R:
        if not r["ok"]: print("FAIL",r["cat"],r["i"],r.get("err") or r.get("out"))
    json.dump({"summary":summ,"results":R},open(os.path.join(os.path.dirname(os.path.abspath(__file__)),f"results-{summ['date']}.json"),"w"),indent=1)
