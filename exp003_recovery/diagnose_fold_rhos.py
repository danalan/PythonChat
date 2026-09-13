import json
from datetime import datetime
import parlay_replay_dc as p

allm=p.load_all()
# Chronological training sizes documented by original validation artifact.
# Use the first N rows from the same canonical chronological source.
TARGET={
  343:{90:-0.083682295276327,180:-0.1097412120390276,365:-0.1233508682079011,730:-0.1295006123719428,1460:-0.1323914071230084},
  510:{90:-0.061727111232461,180:-0.0962143976814364,365:-0.1143729910956522,730:-0.1229079106146276,1460:-0.1269702803506494},
  678:{90:-0.0584896246773078,180:-0.0716776088475166,365:-0.0884774367846064,730:-0.0987337429031691,1460:-0.1040874268840633},
}
# as-of at first validation row, so decay ages mirror walk-forward training boundary.
ASOF={343:allm[343].date,510:allm[510].date,678:allm[678].date}
out=[]
for n in (343,510,678):
  tr=allm[:n]
  for hl in (90.,180.,365.,730.,1460.):
    m=p.DCModel(tr,ASOF[n],hl).fit()
    rho=float(m.unpack(m.theta)[-1])
    target=TARGET[n][int(hl)]
    out.append({'n':n,'asof':ASOF[n].isoformat(),'half_life':hl,'rho':rho,'target':target,'error':rho-target,'fit':m.fit_result})
print(json.dumps(out,ensure_ascii=False,indent=2))
