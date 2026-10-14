// LENNON PURE GOALS — independent Poisson V0.1, deterministic reconstruction.
// Inputs are domestic xG/xGA per match, NOT calibrated across leagues.
// Historical Poisson-v0.1 formula: lambdaH=(home.xG+away.xGA)/2;
// lambdaA=(away.xG+home.xGA)/2. No market prices enter model.
// Must use genuine pre-kickoff inputs; NEVER retrofreeze or treat as LIVE edge.
export function predictGoals(home, away, maxGoals=19) {
  if (![home.xg,home.xga,away.xg,away.xga].every(x=>Number.isFinite(x)&&x>=0)) throw new Error("bad inputs");
  const lh=(home.xg+away.xga)/2, la=(away.xg+home.xga)/2;
  const poisson=(lam)=>{let p=[Math.exp(-lam)];for(let k=1;k<=maxGoals;k++)p.push(p[k-1]*lam/k);return p};
  const ph=poisson(lh), pa=poisson(la);
  let h=0,d=0,a=0,o25=0,btts=0,home15=0,away15=0,ahm1win=0,ahm1push=0;
  for(let i=0;i<=maxGoals;i++)for(let j=0;j<=maxGoals;j++){
    const v=ph[i]*pa[j];
    if(i>j)h+=v;else if(i===j)d+=v;else a+=v;
    if(i+j>=3)o25+=v;
    if(i>=1&&j>=1)btts+=v;
    if(i>=2)home15+=v;if(j>=2)away15+=v;
    if(i-j>=2)ahm1win+=v;if(i-j===1)ahm1push+=v;
  }
  const z=h+d+a;h/=z;d/=z;a/=z;
  return {lambda_home:lh,lambda_away:la,
    p1x2:{home:h,draw:d,away:a},
    ou25:{over2_5:o25/z,under2_5:1-o25/z},
    btts:{yes:btts/z,no:1-btts/z},
    dc:{"1X":h+d,X2:a+d,"12":h+a},
    dnb:{home:h/(h+a),away:a/(h+a),push:d},
    team_ou15:{home_over1_5:home15/z,away_over1_5:away15/z},
    asian_home_minus1:{win:ahm1win/z,push:ahm1push/z,lose:1-(ahm1win+ahm1push)/z}
  };
}
