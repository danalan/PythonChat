import re, math, json
from datetime import datetime
import numpy as np
from scipy.special import gammaln
import parlay_replay_dc as p

# Reparse same OpenFootball sources but retain HH:MM where present.
def parse_with_time(text, source):
    mseason=re.search(r'(20\d{2})-(\d{2})',source); sy=int(mseason.group(1)); ey=2000+int(mseason.group(2))
    date_parts=None; out=[]
    for raw in text.splitlines():
        dm=p.DATE_RE.match(raw)
        if dm:
            mon,day,explicit=dm.groups(); month=p.MONTHS[mon]; year=int(explicit) if explicit else (sy if month>=6 else ey); date_parts=(year,month,int(day)); continue
        mm=p.MATCH_RE.match(raw)
        if not mm or date_parts is None: continue
        tm,home,away,hg,ag,tail=mm.groups()
        if 'pen' in tail.lower() or 'shoot' in tail.lower(): continue
        hh,mi=(0,0)
        if tm:
            hh,mi=map(int,tm.split(':'))
        dt=datetime(*date_parts,hh,mi)
        out.append(p.Match(dt,home.strip(),away.strip(),int(hg),int(ag),source))
    return out

def load():
    rows=[]
    for f in p.FILES: rows += parse_with_time(p.fetch_text(f),f)
    seen=set(); ded=[]
    for r in sorted(rows,key=lambda x:(x.date,x.home,x.away,x.hg,x.ag)):
        k=(r.date.isoformat(),r.home,r.away,r.hg,r.ag)
        if k not in seen: seen.add(k);ded.append(r)
    return ded

ALL=load(); TR=[m for m in ALL if m.date < datetime(2025,1,10)]; ASOF=datetime(2025,1,10)
FIX={'J1-01':('Gallos Blancos','CF América'),'J1-03':('Club Tijuana','Deportivo Toluca'),'J1-05':('CF Monterrey','Puebla FC'),'J1-06':('Deportivo Guadalajara','Santos Laguna'),'J1-08':('Pumas UNAM','Club Necaxa')}
REF={
'J1-01':{'HOME':.1528465072043198,'DRAW':.2448419924548112,'AWAY':.6023115003408691,'OVER_2.5':.4804085691075246},
'J1-03':{'HOME':.2815287030638931,'DRAW':.2482744414842101,'AWAY':.4701968554518968,'OVER_2.5':.6083459289781771},
'J1-05':{'HOME':.7678854037252519,'DRAW':.1525191559096011,'AWAY':.0795954403651469,'OVER_2.5':.6720335112737199},
'J1-06':{'HOME':.6301823415365048,'DRAW':.2340571514348059,'AWAY':.1357605070286892,'OVER_2.5':.4854615882568141},
'J1-08':{'HOME':.5738052229420694,'DRAW':.2427365839689352,'AWAY':.1834581930889955,'OVER_2.5':.5333926985861029}}
mods=p.ensemble(TR,ASOF)
def mprobs(M):
    return {'HOME':float(np.tril(M,-1).sum()),'DRAW':float(np.trace(M)),'AWAY':float(np.triu(M,1).sum()),'OVER_2.5':float(sum(M[i,j] for i in range(M.shape[0]) for j in range(M.shape[1]) if i+j>=3))}
errs=[];out={}
for fid,(h,a) in FIX.items():
    M,_=p.avg_matrix(mods,h,a);g=mprobs(M);out[fid]={}
    for k,t in REF[fid].items():out[fid][k]={'got':g[k],'target':t,'err':g[k]-t};errs.append(abs(g[k]-t))
print(json.dumps({'count':len(TR),'mae':float(np.mean(errs)),'maxae':float(np.max(errs)),'rows':out},ensure_ascii=False,indent=2))
