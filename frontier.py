import json,math,sys
d=json.load(open(sys.argv[1]))
def front(pts):
    pts=sorted([p for p in pts if p[3] and p[4] is not None],key=lambda p:(p[3],-p[4]))
    f=[];best=-1e9
    for p in pts:
        if p[4]>best: f.append(p);best=p[4]
    return f
B={'index':'Intelligence Index','tb':'Terminal-Bench (coding)','ab':'AutomationBench (tool workflows)','gdp':'GDPval (knowledge work)','omni':'AA-Omniscience (fact reliability)','hle':'HLE (reasoning)'}
for k,n in B.items():
    pts=[(p['vendor'],p['model'],p['effort'],p['cost'],p[k]) for p in d['aa']]
    print('\n##',n,'(AA, cost per Index task)')
    f=front(pts);prev=None
    for p in f:
        g='' if not prev else f"  +{p[4]-prev[4]} for x{p[3]/prev[3]:.1f} cost = {(p[4]-prev[4])/math.log2(p[3]/prev[3]):.1f}/doubling"
        print(f"  {p[1]} {p[2]}: {p[4]} @ ${p[3]}{g}");prev=p
for k,v in d['vendor_charts'].items():
    print('\n##',v['label'],'(vendor chart)')
    f=front([tuple(x) for x in v['points']]);prev=None
    for p in f:
        g='' if not prev else f"  +{p[4]-prev[4]:.1f} for x{p[3]/prev[3]:.1f} = {(p[4]-prev[4])/math.log2(p[3]/prev[3]):.1f}/doubling"
        print(f"  {p[1]} {p[2]}: {p[4]} @ ${p[3]}{g}");prev=p
