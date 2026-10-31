from promotions import effective_cost
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
    # Retired benchmarks (v4.3.2) pair with legacy_cost. Withheld rows lack a v5.0 row and skip current charts.
    legacy=k in ('gdp','sci','hle');held=set(d.get('aa_current_version_withheld',{}).get('rows',[]))
    pts=[(p['vendor'],p['model'],p['effort'],p['legacy_cost'] if legacy and 'legacy_cost' in p else effective_cost(p,d.get('promotions',[])),p[k]) for p in d['aa']
         if legacy or f"{p['vendor']}|{p['model']}|{p['effort']}" not in held]
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
