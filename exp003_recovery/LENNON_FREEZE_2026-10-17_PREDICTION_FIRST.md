# LENNON prospective freeze — 17 October 2026

**Run ID:** LENNON-2026-10-17-PREDICTION-FIRST. **Cutoff:** 2026-10-17T08:52:43-06:00 CDMX, recorded after CP/Master reads and before web slate research. **Freeze:** 2026-10-17T08:56:23-06:00 CDMX, prior to all listed kickoffs. **REAL=0; SHADOW=0; parlays=0.**

Canonical CP `LENNON Prediction Ledger!A225:AE240`, readback verified. Eight 16-Oct settlements first in `A217:AE224`. Model `LENNON-PURE-GOALS-POISSON-V0.1-JS-REPRO` (independent Poisson 0..19; lambdaH=(home xG+away xGA)/2, lambdaA=(away xG+home xGA)/2). The 16 forecasts use verified pre-match xG/xGA feature values from linked vendor pages, **not** bookmaker probabilities. Source snapshot was retrieved after cutoff but before kickoff; vendor historical point-in-time archives not independently certified. Tifolab domestic season sample sizes and Footboom last-ten mixed competition inputs are heterogeneous. No home adjustment or opponent-strength calibration. These are experimental, not betting recommendations. No verified timestamped bookmaker odds => NO validated edge, NO SHADOW. MARKET-AWARE, Corners, Shots/SOT, Cards NOT executed. Player props, fouls, offsides, throw-ins, goal kicks research-only. No exhaustive global slate claim: games already started at freeze and unverified/incomplete-data fixtures excluded.

| Fixture | League | Kickoff CDMX | λ home/away | P(1/X/2) | Classification |
|---|---|---|---|---|---|
| 2026-10-17|SAN-QUE | Liga MX | 17:00 CDMX | 1.530/1.645 | 35.8/23.5/40.7 | FORECAST_ONLY |
| 2026-10-17|GUA-TIG | Liga MX | 17:07 CDMX | 1.565/1.325 | 43.0/24.6/32.3 | FORECAST_ONLY |
| 2026-10-17|LEO-AME | Liga MX | 19:00 CDMX | 1.415/1.550 | 34.8/24.4/40.8 | FORECAST_ONLY |
| 2026-10-17|TOL-ASL | Liga MX | 19:00 CDMX | 1.720/1.180 | 50.0/23.8/26.2 | FORECAST_ONLY |
| 2026-10-17|CAZ-JUA | Liga MX | 21:10 CDMX | 1.975/1.130 | 57.0/21.7/21.4 | FORECAST_ONLY |
| 2026-10-17|STR-PSG | Ligue 1 | 09:15 CDMX | 1.400/2.155 | 24.6/20.6/54.8 | FORECAST_ONLY |
| 2026-10-17|BOL-INT | Serie A | 10:00 CDMX | 1.395/1.885 | 28.5/22.4/49.1 | FORECAST_ONLY |
| 2026-10-17|NEW-AVL | Premier League | 10:30 CDMX | 1.450/1.645 | 33.9/23.8/42.3 | FORECAST_ONLY |
| 2026-10-17|BAY-RBL | Bundesliga | 10:30 CDMX | 2.220/1.540 | 53.1/20.3/26.6 | FORECAST_ONLY |
| 2026-10-17|BET-BAR | La Liga | 10:30 CDMX | 1.350/2.000 | 25.8/21.7/52.6 | FORECAST_ONLY |
| 2026-10-17|ROM-GEN | Serie A | 12:45 CDMX | 1.880/1.215 | 52.9/22.5/24.6 | FORECAST_ONLY |
| 2026-10-17|TRO-LEN | Ligue 1 | 12:45 CDMX | 1.555/1.650 | 36.3/23.4/40.3 | FORECAST_ONLY |
| 2026-10-17|LIL-BRE | Ligue 1 | 12:45 CDMX | 1.275/1.960 | 24.7/21.9/53.4 | FORECAST_ONLY |
| 2026-10-17|TEL-FEY | Eredivisie | 12:00 CDMX | 1.190/1.940 | 23.1/22.0/54.8 | FORECAST_ONLY |
| 2026-10-17|PHI-CLT | MLS | 12:30 CDMX | 2.135/1.355 | 55.3/20.7/24.0 | FORECAST_ONLY |
| 2026-10-17|MIN-STL | MLS | 14:30 CDMX | 1.430/1.605 | 34.2/24.0/41.8 | FORECAST_ONLY |

**Full-precision canonical CP mirror** (not a retrofreeze):

```json
{
  "run_id": "LENNON-2026-10-17-PREDICTION-FIRST",
  "cutoff": "2026-10-17T08:52:43-06:00",
  "freeze": "2026-10-17T08:56:23-06:00",
  "forecasts": [
    {
      "record_id": "LEN17-SAN-QUE",
      "run_date": "2026-10-17",
      "record_type": "FREEZE_PROSPECTIVE",
      "fixture_key": "2026-10-17|SAN-QUE",
      "competition": "Liga MX",
      "kickoff_cdmx": "2026-10-17 17:00 CDMX",
      "cutoff_cdmx": "2026-10-17T08:52:43-06:00",
      "freeze_cdmx": "2026-10-17T08:56:23-06:00",
      "model_version": "LENNON-PURE-GOALS-POISSON-V0.1-JS-REPRO",
      "features": {
        "home_xg": 1.55,
        "home_xga": 1.66,
        "away_xg": 1.63,
        "away_xga": 1.51
      },
      "lambda_home": 1.53,
      "lambda_away": 1.645,
      "p1x2": {
        "home": 0.35790565987073003,
        "draw": 0.2349054416341387,
        "away": 0.40718889849513135
      },
      "ou25": {
        "over2_5": 0.6148542701999355,
        "under2_5": 0.38514572980006445
      },
      "btts": {
        "yes": 0.6322458739751505,
        "no": 0.36775412602484947
      },
      "dc": {
        "12": 0.7650945583658614,
        "1X": 0.5928111015048687,
        "X2": 0.64209434012927
      },
      "dnb": {
        "home": 0.46779271392959343,
        "away": 0.5322072860704066,
        "push": 0.2349054416341387
      },
      "team_ou15": {
        "home_over1_5": 0.45216476169050174,
        "away_over1_5": 0.48948177141049937
      },
      "odds": {
        "status": "NO_VERIFIED_BOOKMAKER_QUOTE",
        "odds": null,
        "operator": null,
        "observed_timestamp": null
      },
      "market_no_vig": {
        "status": "NO_VALID_QUOTE",
        "market_no_vig": null
      },
      "edge": {
        "validated_edge": false,
        "edge_pp": null,
        "reason": "NO_VERIFIED_BOOKMAKER_QUOTE"
      },
      "classification": "FORECAST_ONLY",
      "settlement": "PENDING",
      "notes": "Santos Laguna vs Querétaro; source https://www.tifolab.com/matches/1550997; provenance TIFOLAB_SEASON_11_10; pre-match source snapshot viewed after cutoff before kickoff; inputs home xG=1.55 xGA=1.66 away xG=1.63 xGA=1.51; independent Poisson 0..19; Asian home -1 {\"win\":0.1716855038988619,\"push\":0.18622015597186833,\"lose\":0.6420943401292698}; no opponent-strength/home advantage calibration, sample heterogeneity, point-in-time vendor data not independently archived. No validated operator/time-stamped odds, no market-aware, corners, SOT, cards; no SHADOW/REAL. Schedules https://www.informador.mx/amp/deportes/futbol-hoy-en-vivo-calendario-de-partidos-del-17-de-octubre-de-2026-canales-horarios-streaming-20261016-0042.html ; https://www.skysports.com/football-scores-fixtures/2026-10-17"
    },
    {
      "record_id": "LEN17-GUA-TIG",
      "run_date": "2026-10-17",
      "record_type": "FREEZE_PROSPECTIVE",
      "fixture_key": "2026-10-17|GUA-TIG",
      "competition": "Liga MX",
      "kickoff_cdmx": "2026-10-17 17:07 CDMX",
      "cutoff_cdmx": "2026-10-17T08:52:43-06:00",
      "freeze_cdmx": "2026-10-17T08:56:23-06:00",
      "model_version": "LENNON-PURE-GOALS-POISSON-V0.1-JS-REPRO",
      "features": {
        "home_xg": 1.59,
        "home_xga": 1.08,
        "away_xg": 1.57,
        "away_xga": 1.54
      },
      "lambda_home": 1.565,
      "lambda_away": 1.3250000000000002,
      "p1x2": {
        "home": 0.4304083890766033,
        "draw": 0.24626962709992764,
        "away": 0.32332198382346916
      },
      "ou25": {
        "over2_5": 0.5517194902651469,
        "under2_5": 0.4482805097348531
      },
      "btts": {
        "yes": 0.5806852403492735,
        "no": 0.4193147596507265
      },
      "dc": {
        "12": 0.7537303729000724,
        "1X": 0.6766780161765309,
        "X2": 0.5695916109233968
      },
      "dnb": {
        "home": 0.5710376078126623,
        "away": 0.4289623921873377,
        "push": 0.24626962709992764
      },
      "team_ou15": {
        "home_over1_5": 0.4636892462105287,
        "away_over1_5": 0.38200812011824564
      },
      "odds": {
        "status": "NO_VERIFIED_BOOKMAKER_QUOTE",
        "odds": null,
        "operator": null,
        "observed_timestamp": null
      },
      "market_no_vig": {
        "status": "NO_VALID_QUOTE",
        "market_no_vig": null
      },
      "edge": {
        "validated_edge": false,
        "edge_pp": null,
        "reason": "NO_VERIFIED_BOOKMAKER_QUOTE"
      },
      "classification": "FORECAST_ONLY",
      "settlement": "PENDING",
      "notes": "Guadalajara vs Tigres; source https://www.tifolab.com/matches/1550996; provenance TIFOLAB_SEASON_11_11; pre-match source snapshot viewed after cutoff before kickoff; inputs home xG=1.59 xGA=1.08 away xG=1.57 xGA=1.54; independent Poisson 0..19; Asian home -1 {\"win\":0.21610238575901639,\"push\":0.21430600331758712,\"lose\":0.5695916109233965}; no opponent-strength/home advantage calibration, sample heterogeneity, point-in-time vendor data not independently archived. No validated operator/time-stamped odds, no market-aware, corners, SOT, cards; no SHADOW/REAL. Schedules https://www.informador.mx/amp/deportes/futbol-hoy-en-vivo-calendario-de-partidos-del-17-de-octubre-de-2026-canales-horarios-streaming-20261016-0042.html ; https://www.skysports.com/football-scores-fixtures/2026-10-17"
    },
    {
      "record_id": "LEN17-LEO-AME",
      "run_date": "2026-10-17",
      "record_type": "FREEZE_PROSPECTIVE",
      "fixture_key": "2026-10-17|LEO-AME",
      "competition": "Liga MX",
      "kickoff_cdmx": "2026-10-17 19:00 CDMX",
      "cutoff_cdmx": "2026-10-17T08:52:43-06:00",
      "freeze_cdmx": "2026-10-17T08:56:23-06:00",
      "model_version": "LENNON-PURE-GOALS-POISSON-V0.1-JS-REPRO",
      "features": {
        "home_xg": 1.39,
        "home_xga": 1.36,
        "away_xg": 1.74,
        "away_xga": 1.44
      },
      "lambda_home": 1.415,
      "lambda_away": 1.55,
      "p1x2": {
        "home": 0.3481635898146391,
        "draw": 0.244026504250402,
        "away": 0.40780990593495886
      },
      "ou25": {
        "over2_5": 0.5689228963234326,
        "under2_5": 0.4310771036765674
      },
      "btts": {
        "yes": 0.596386881969629,
        "no": 0.40361311803037103
      },
      "dc": {
        "12": 0.7559734957495979,
        "1X": 0.5921900940650411,
        "X2": 0.6518364101853609
      },
      "dnb": {
        "home": 0.46054999516803397,
        "away": 0.539450004831966,
        "push": 0.244026504250402
      },
      "team_ou15": {
        "home_over1_5": 0.4133346435212867,
        "away_over1_5": 0.45876766674180464
      },
      "odds": {
        "status": "NO_VERIFIED_BOOKMAKER_QUOTE",
        "odds": null,
        "operator": null,
        "observed_timestamp": null
      },
      "market_no_vig": {
        "status": "NO_VALID_QUOTE",
        "market_no_vig": null
      },
      "edge": {
        "validated_edge": false,
        "edge_pp": null,
        "reason": "NO_VERIFIED_BOOKMAKER_QUOTE"
      },
      "classification": "FORECAST_ONLY",
      "settlement": "PENDING",
      "notes": "León vs América; source https://www.tifolab.com/matches/1550998; provenance TIFOLAB_SEASON_11_10; pre-match source snapshot viewed after cutoff before kickoff; inputs home xG=1.39 xGA=1.36 away xG=1.74 xGA=1.44; independent Poisson 0..19; Asian home -1 {\"win\":0.15997505899794998,\"push\":0.18818853081668924,\"lose\":0.6518364101853609}; no opponent-strength/home advantage calibration, sample heterogeneity, point-in-time vendor data not independently archived. No validated operator/time-stamped odds, no market-aware, corners, SOT, cards; no SHADOW/REAL. Schedules https://www.informador.mx/amp/deportes/futbol-hoy-en-vivo-calendario-de-partidos-del-17-de-octubre-de-2026-canales-horarios-streaming-20261016-0042.html ; https://www.skysports.com/football-scores-fixtures/2026-10-17"
    },
    {
      "record_id": "LEN17-TOL-ASL",
      "run_date": "2026-10-17",
      "record_type": "FREEZE_PROSPECTIVE",
      "fixture_key": "2026-10-17|TOL-ASL",
      "competition": "Liga MX",
      "kickoff_cdmx": "2026-10-17 19:00 CDMX",
      "cutoff_cdmx": "2026-10-17T08:52:43-06:00",
      "freeze_cdmx": "2026-10-17T08:56:23-06:00",
      "model_version": "LENNON-PURE-GOALS-POISSON-V0.1-JS-REPRO",
      "features": {
        "home_xg": 1.94,
        "home_xga": 1.11,
        "away_xg": 1.25,
        "away_xga": 1.5
      },
      "lambda_home": 1.72,
      "lambda_away": 1.1800000000000002,
      "p1x2": {
        "home": 0.5002239161546302,
        "draw": 0.23790092382633432,
        "away": 0.2618751600190355
      },
      "ou25": {
        "over2_5": 0.5540368014428179,
        "under2_5": 0.44596319855718214
      },
      "btts": {
        "yes": 0.5686783335437827,
        "no": 0.4313216664562173
      },
      "dc": {
        "12": 0.7620990761736657,
        "1X": 0.7381248399809646,
        "X2": 0.4997760838453698
      },
      "dnb": {
        "home": 0.6563764893485321,
        "away": 0.34362351065146796,
        "push": 0.23790092382633432
      },
      "team_ou15": {
        "home_over1_5": 0.5129400776807365,
        "away_over1_5": 0.330132349849534
      },
      "odds": {
        "status": "NO_VERIFIED_BOOKMAKER_QUOTE",
        "odds": null,
        "operator": null,
        "observed_timestamp": null
      },
      "market_no_vig": {
        "status": "NO_VALID_QUOTE",
        "market_no_vig": null
      },
      "edge": {
        "validated_edge": false,
        "edge_pp": null,
        "reason": "NO_VERIFIED_BOOKMAKER_QUOTE"
      },
      "classification": "FORECAST_ONLY",
      "settlement": "PENDING",
      "notes": "Toluca vs Atlético San Luis; source https://www.tifolab.com/matches/1550999; provenance TIFOLAB_SEASON_11_11; pre-match source snapshot viewed after cutoff before kickoff; inputs home xG=1.94 xGA=1.11 away xG=1.25 xGA=1.5; independent Poisson 0..19; Asian home -1 {\"win\":0.2709641238161635,\"push\":0.2292597923384666,\"lose\":0.49977608384536987}; no opponent-strength/home advantage calibration, sample heterogeneity, point-in-time vendor data not independently archived. No validated operator/time-stamped odds, no market-aware, corners, SOT, cards; no SHADOW/REAL. Schedules https://www.informador.mx/amp/deportes/futbol-hoy-en-vivo-calendario-de-partidos-del-17-de-octubre-de-2026-canales-horarios-streaming-20261016-0042.html ; https://www.skysports.com/football-scores-fixtures/2026-10-17"
    },
    {
      "record_id": "LEN17-CAZ-JUA",
      "run_date": "2026-10-17",
      "record_type": "FREEZE_PROSPECTIVE",
      "fixture_key": "2026-10-17|CAZ-JUA",
      "competition": "Liga MX",
      "kickoff_cdmx": "2026-10-17 21:10 CDMX",
      "cutoff_cdmx": "2026-10-17T08:52:43-06:00",
      "freeze_cdmx": "2026-10-17T08:56:23-06:00",
      "model_version": "LENNON-PURE-GOALS-POISSON-V0.1-JS-REPRO",
      "features": {
        "home_xg": 1.87,
        "home_xga": 1.35,
        "away_xg": 0.91,
        "away_xga": 2.08
      },
      "lambda_home": 1.975,
      "lambda_away": 1.1300000000000001,
      "p1x2": {
        "home": 0.5697739098291984,
        "draw": 0.2166305840957828,
        "away": 0.21359550607501887
      },
      "ou25": {
        "over2_5": 0.5999181992927608,
        "under2_5": 0.4000818007072392
      },
      "btts": {
        "yes": 0.5830299498940537,
        "no": 0.41697005010594634
      },
      "dc": {
        "12": 0.7833694159042173,
        "1X": 0.7864044939249812,
        "X2": 0.4302260901708017
      },
      "dnb": {
        "home": 0.7273374454777857,
        "away": 0.2726625545222144,
        "push": 0.2166305840957828
      },
      "team_ou15": {
        "home_over1_5": 0.5871850960771867,
        "away_over1_5": 0.31193916382060094
      },
      "odds": {
        "status": "NO_VERIFIED_BOOKMAKER_QUOTE",
        "odds": null,
        "operator": null,
        "observed_timestamp": null
      },
      "market_no_vig": {
        "status": "NO_VALID_QUOTE",
        "market_no_vig": null
      },
      "edge": {
        "validated_edge": false,
        "edge_pp": null,
        "reason": "NO_VERIFIED_BOOKMAKER_QUOTE"
      },
      "classification": "FORECAST_ONLY",
      "settlement": "PENDING",
      "notes": "Cruz Azul vs Juárez; source https://www.tifolab.com/matches/1551000; provenance TIFOLAB_SEASON_10_10; pre-match source snapshot viewed after cutoff before kickoff; inputs home xG=1.87 xGA=1.35 away xG=0.91 xGA=2.08; independent Poisson 0..19; Asian home -1 {\"win\":0.3380581721808683,\"push\":0.23171573764833003,\"lose\":0.4302260901708016}; no opponent-strength/home advantage calibration, sample heterogeneity, point-in-time vendor data not independently archived. No validated operator/time-stamped odds, no market-aware, corners, SOT, cards; no SHADOW/REAL. Schedules https://www.informador.mx/amp/deportes/futbol-hoy-en-vivo-calendario-de-partidos-del-17-de-octubre-de-2026-canales-horarios-streaming-20261016-0042.html ; https://www.skysports.com/football-scores-fixtures/2026-10-17"
    },
    {
      "record_id": "LEN17-STR-PSG",
      "run_date": "2026-10-17",
      "record_type": "FREEZE_PROSPECTIVE",
      "fixture_key": "2026-10-17|STR-PSG",
      "competition": "Ligue 1",
      "kickoff_cdmx": "2026-10-17 09:15 CDMX",
      "cutoff_cdmx": "2026-10-17T08:52:43-06:00",
      "freeze_cdmx": "2026-10-17T08:56:23-06:00",
      "model_version": "LENNON-PURE-GOALS-POISSON-V0.1-JS-REPRO",
      "features": {
        "home_xg": 1.38,
        "home_xga": 1.71,
        "away_xg": 2.6,
        "away_xga": 1.42
      },
      "lambda_home": 1.4,
      "lambda_away": 2.1550000000000002,
      "p1x2": {
        "home": 0.24610604893761232,
        "draw": 0.2063044114837522,
        "away": 0.5475895395786355
      },
      "ou25": {
        "over2_5": 0.6892057718930951,
        "under2_5": 0.31079422810690494
      },
      "btts": {
        "yes": 0.6660812203617745,
        "no": 0.33391877963822547
      },
      "dc": {
        "12": 0.7936955885162479,
        "1X": 0.4524104604213645,
        "X2": 0.7538939510623878
      },
      "dnb": {
        "home": 0.3100761204905881,
        "away": 0.6899238795094118,
        "push": 0.2063044114837522
      },
      "team_ou15": {
        "home_over1_5": 0.4081672865401441,
        "away_over1_5": 0.6343254336162774
      },
      "odds": {
        "status": "NO_VERIFIED_BOOKMAKER_QUOTE",
        "odds": null,
        "operator": null,
        "observed_timestamp": null
      },
      "market_no_vig": {
        "status": "NO_VALID_QUOTE",
        "market_no_vig": null
      },
      "edge": {
        "validated_edge": false,
        "edge_pp": null,
        "reason": "NO_VERIFIED_BOOKMAKER_QUOTE"
      },
      "classification": "FORECAST_ONLY",
      "settlement": "PENDING",
      "notes": "Strasbourg vs PSG; source https://www.footboom1.com/br/football/game/strasbourg-psg-2026-10-17; provenance FOOTBOOM_LAST10_MIXED; pre-match source snapshot viewed after cutoff before kickoff; inputs home xG=1.38 xGA=1.71 away xG=2.6 xGA=1.42; independent Poisson 0..19; Asian home -1 {\"win\":0.10647304783080191,\"push\":0.1396330011068104,\"lose\":0.7538939510623877}; no opponent-strength/home advantage calibration, sample heterogeneity, point-in-time vendor data not independently archived. No validated operator/time-stamped odds, no market-aware, corners, SOT, cards; no SHADOW/REAL. Schedules https://www.informador.mx/amp/deportes/futbol-hoy-en-vivo-calendario-de-partidos-del-17-de-octubre-de-2026-canales-horarios-streaming-20261016-0042.html ; https://www.skysports.com/football-scores-fixtures/2026-10-17"
    },
    {
      "record_id": "LEN17-BOL-INT",
      "run_date": "2026-10-17",
      "record_type": "FREEZE_PROSPECTIVE",
      "fixture_key": "2026-10-17|BOL-INT",
      "competition": "Serie A",
      "kickoff_cdmx": "2026-10-17 10:00 CDMX",
      "cutoff_cdmx": "2026-10-17T08:52:43-06:00",
      "freeze_cdmx": "2026-10-17T08:56:23-06:00",
      "model_version": "LENNON-PURE-GOALS-POISSON-V0.1-JS-REPRO",
      "features": {
        "home_xg": 1.11,
        "home_xga": 1.02,
        "away_xg": 2.75,
        "away_xga": 1.68
      },
      "lambda_home": 1.395,
      "lambda_away": 1.885,
      "p1x2": {
        "home": 0.28534393531597146,
        "draw": 0.2241036108959117,
        "away": 0.4905524537881168
      },
      "ou25": {
        "over2_5": 0.6365411418481157,
        "under2_5": 0.3634588581518843
      },
      "btts": {
        "yes": 0.6379661610105148,
        "no": 0.36203383898948516
      },
      "dc": {
        "12": 0.7758963891040882,
        "1X": 0.5094475462118832,
        "X2": 0.7146560646840285
      },
      "dnb": {
        "home": 0.3677603599179683,
        "away": 0.6322396400820317,
        "push": 0.2241036108959117
      },
      "team_ou15": {
        "home_over1_5": 0.40643987790048686,
        "away_over1_5": 0.5619731635460832
      },
      "odds": {
        "status": "NO_VERIFIED_BOOKMAKER_QUOTE",
        "odds": null,
        "operator": null,
        "observed_timestamp": null
      },
      "market_no_vig": {
        "status": "NO_VALID_QUOTE",
        "market_no_vig": null
      },
      "edge": {
        "validated_edge": false,
        "edge_pp": null,
        "reason": "NO_VERIFIED_BOOKMAKER_QUOTE"
      },
      "classification": "FORECAST_ONLY",
      "settlement": "PENDING",
      "notes": "Bologna vs Inter; source https://www.footboom1.com/hr/football/game/bologna-inter-2026-10-18; provenance FOOTBOOM_LAST10_MIXED; pre-match source snapshot viewed after cutoff before kickoff; inputs home xG=1.11 xGA=1.02 away xG=2.75 xGA=1.68; independent Poisson 0..19; Asian home -1 {\"win\":0.12600990301364698,\"push\":0.15933403230232474,\"lose\":0.7146560646840283}; no opponent-strength/home advantage calibration, sample heterogeneity, point-in-time vendor data not independently archived. No validated operator/time-stamped odds, no market-aware, corners, SOT, cards; no SHADOW/REAL. Schedules https://www.informador.mx/amp/deportes/futbol-hoy-en-vivo-calendario-de-partidos-del-17-de-octubre-de-2026-canales-horarios-streaming-20261016-0042.html ; https://www.skysports.com/football-scores-fixtures/2026-10-17"
    },
    {
      "record_id": "LEN17-NEW-AVL",
      "run_date": "2026-10-17",
      "record_type": "FREEZE_PROSPECTIVE",
      "fixture_key": "2026-10-17|NEW-AVL",
      "competition": "Premier League",
      "kickoff_cdmx": "2026-10-17 10:30 CDMX",
      "cutoff_cdmx": "2026-10-17T08:52:43-06:00",
      "freeze_cdmx": "2026-10-17T08:56:23-06:00",
      "model_version": "LENNON-PURE-GOALS-POISSON-V0.1-JS-REPRO",
      "features": {
        "home_xg": 1.38,
        "home_xga": 1.51,
        "away_xg": 1.78,
        "away_xga": 1.52
      },
      "lambda_home": 1.45,
      "lambda_away": 1.645,
      "p1x2": {
        "home": 0.33900605988064547,
        "draw": 0.237535342952062,
        "away": 0.4234585971672925
      },
      "ou25": {
        "over2_5": 0.5977535858592091,
        "under2_5": 0.4022464141407909
      },
      "btts": {
        "yes": 0.6176921615726954,
        "no": 0.38230783842730465
      },
      "dc": {
        "12": 0.762464657047938,
        "1X": 0.5765414028327075,
        "X2": 0.6609939401193545
      },
      "dnb": {
        "home": 0.44461872002459435,
        "away": 0.5553812799754057,
        "push": 0.237535342952062
      },
      "team_ou15": {
        "home_over1_5": 0.4253027941701956,
        "away_over1_5": 0.4894817714104993
      },
      "odds": {
        "status": "NO_VERIFIED_BOOKMAKER_QUOTE",
        "odds": null,
        "operator": null,
        "observed_timestamp": null
      },
      "market_no_vig": {
        "status": "NO_VALID_QUOTE",
        "market_no_vig": null
      },
      "edge": {
        "validated_edge": false,
        "edge_pp": null,
        "reason": "NO_VERIFIED_BOOKMAKER_QUOTE"
      },
      "classification": "FORECAST_ONLY",
      "settlement": "PENDING",
      "notes": "Newcastle vs Aston Villa; source https://www.footboom1.com/br/football/game/newcastle-aston-villa-2026-10-17; provenance FOOTBOOM_LAST10_MIXED; pre-match source snapshot viewed after cutoff before kickoff; inputs home xG=1.38 xGA=1.51 away xG=1.78 xGA=1.52; independent Poisson 0..19; Asian home -1 {\"win\":0.1569508658837014,\"push\":0.182055193996944,\"lose\":0.6609939401193545}; no opponent-strength/home advantage calibration, sample heterogeneity, point-in-time vendor data not independently archived. No validated operator/time-stamped odds, no market-aware, corners, SOT, cards; no SHADOW/REAL. Schedules https://www.informador.mx/amp/deportes/futbol-hoy-en-vivo-calendario-de-partidos-del-17-de-octubre-de-2026-canales-horarios-streaming-20261016-0042.html ; https://www.skysports.com/football-scores-fixtures/2026-10-17"
    },
    {
      "record_id": "LEN17-BAY-RBL",
      "run_date": "2026-10-17",
      "record_type": "FREEZE_PROSPECTIVE",
      "fixture_key": "2026-10-17|BAY-RBL",
      "competition": "Bundesliga",
      "kickoff_cdmx": "2026-10-17 10:30 CDMX",
      "cutoff_cdmx": "2026-10-17T08:52:43-06:00",
      "freeze_cdmx": "2026-10-17T08:56:23-06:00",
      "model_version": "LENNON-PURE-GOALS-POISSON-V0.1-JS-REPRO",
      "features": {
        "home_xg": 3.08,
        "home_xga": 0.77,
        "away_xg": 2.31,
        "away_xga": 1.36
      },
      "lambda_home": 2.22,
      "lambda_away": 1.54,
      "p1x2": {
        "home": 0.5313320303961497,
        "draw": 0.20312165741239332,
        "away": 0.26554631219145686
      },
      "ou25": {
        "over2_5": 0.724581291853302,
        "under2_5": 0.275418708146698
      },
      "btts": {
        "yes": 0.7002935301229247,
        "no": 0.2997064698770753
      },
      "dc": {
        "12": 0.7968783425876066,
        "1X": 0.734453687808543,
        "X2": 0.46866796960385015
      },
      "dnb": {
        "home": 0.6667668099384149,
        "away": 0.33323319006158514,
        "push": 0.20312165741239332
      },
      "team_ou15": {
        "home_over1_5": 0.6502786695834878,
        "away_over1_5": 0.4554720023754757
      },
      "odds": {
        "status": "NO_VERIFIED_BOOKMAKER_QUOTE",
        "odds": null,
        "operator": null,
        "observed_timestamp": null
      },
      "market_no_vig": {
        "status": "NO_VALID_QUOTE",
        "market_no_vig": null
      },
      "edge": {
        "validated_edge": false,
        "edge_pp": null,
        "reason": "NO_VERIFIED_BOOKMAKER_QUOTE"
      },
      "classification": "FORECAST_ONLY",
      "settlement": "PENDING",
      "notes": "Bayern Munich vs RB Leipzig; source https://www.footboom1.com/en/football/game/bayern-munich-rb-leipzig-2026-10-17; provenance FOOTBOOM_LAST10_MIXED; pre-match source snapshot viewed after cutoff before kickoff; inputs home xG=3.08 xGA=0.77 away xG=2.31 xGA=1.36; independent Poisson 0..19; Asian home -1 {\"win\":0.32383724931253105,\"push\":0.20749478108361882,\"lose\":0.46866796960385015}; no opponent-strength/home advantage calibration, sample heterogeneity, point-in-time vendor data not independently archived. No validated operator/time-stamped odds, no market-aware, corners, SOT, cards; no SHADOW/REAL. Schedules https://www.informador.mx/amp/deportes/futbol-hoy-en-vivo-calendario-de-partidos-del-17-de-octubre-de-2026-canales-horarios-streaming-20261016-0042.html ; https://www.skysports.com/football-scores-fixtures/2026-10-17"
    },
    {
      "record_id": "LEN17-BET-BAR",
      "run_date": "2026-10-17",
      "record_type": "FREEZE_PROSPECTIVE",
      "fixture_key": "2026-10-17|BET-BAR",
      "competition": "La Liga",
      "kickoff_cdmx": "2026-10-17 10:30 CDMX",
      "cutoff_cdmx": "2026-10-17T08:52:43-06:00",
      "freeze_cdmx": "2026-10-17T08:56:23-06:00",
      "model_version": "LENNON-PURE-GOALS-POISSON-V0.1-JS-REPRO",
      "features": {
        "home_xg": 1.9,
        "home_xga": 1.6,
        "away_xg": 2.4,
        "away_xga": 0.8
      },
      "lambda_home": 1.35,
      "lambda_away": 2,
      "p1x2": {
        "home": 0.2577833713673776,
        "draw": 0.2165500675823977,
        "away": 0.5256665610502247
      },
      "ou25": {
        "over2_5": 0.6505159777129352,
        "under2_5": 0.34948402228706477
      },
      "btts": {
        "yes": 0.6405088102183346,
        "no": 0.3594911897816654
      },
      "dc": {
        "12": 0.7834499324176023,
        "1X": 0.4743334389497753,
        "X2": 0.7422166286326224
      },
      "dnb": {
        "home": 0.3290361779366028,
        "away": 0.6709638220633972,
        "push": 0.2165500675823977
      },
      "team_ou15": {
        "home_over1_5": 0.3907853874821548,
        "away_over1_5": 0.5939941502901358
      },
      "odds": {
        "status": "NO_VERIFIED_BOOKMAKER_QUOTE",
        "odds": null,
        "operator": null,
        "observed_timestamp": null
      },
      "market_no_vig": {
        "status": "NO_VALID_QUOTE",
        "market_no_vig": null
      },
      "edge": {
        "validated_edge": false,
        "edge_pp": null,
        "reason": "NO_VERIFIED_BOOKMAKER_QUOTE"
      },
      "classification": "FORECAST_ONLY",
      "settlement": "PENDING",
      "notes": "Real Betis vs Barcelona; source https://www.tipmantips.com/football-stats/match/real-betis-vs-fc-barcelona-17-10-2026/; provenance TIPMANTIPS_PREMATCH_UNSPECIFIED_SAMPLE; pre-match source snapshot viewed after cutoff before kickoff; inputs home xG=1.9 xGA=1.6 away xG=2.4 xGA=0.8; independent Poisson 0..19; Asian home -1 {\"win\":0.1102726856029356,\"push\":0.14751068576444207,\"lose\":0.7422166286326224}; no opponent-strength/home advantage calibration, sample heterogeneity, point-in-time vendor data not independently archived. No validated operator/time-stamped odds, no market-aware, corners, SOT, cards; no SHADOW/REAL. Schedules https://www.informador.mx/amp/deportes/futbol-hoy-en-vivo-calendario-de-partidos-del-17-de-octubre-de-2026-canales-horarios-streaming-20261016-0042.html ; https://www.skysports.com/football-scores-fixtures/2026-10-17"
    },
    {
      "record_id": "LEN17-ROM-GEN",
      "run_date": "2026-10-17",
      "record_type": "FREEZE_PROSPECTIVE",
      "fixture_key": "2026-10-17|ROM-GEN",
      "competition": "Serie A",
      "kickoff_cdmx": "2026-10-17 12:45 CDMX",
      "cutoff_cdmx": "2026-10-17T08:52:43-06:00",
      "freeze_cdmx": "2026-10-17T08:56:23-06:00",
      "model_version": "LENNON-PURE-GOALS-POISSON-V0.1-JS-REPRO",
      "features": {
        "home_xg": 2.08,
        "home_xga": 1.23,
        "away_xg": 1.2,
        "away_xga": 1.68
      },
      "lambda_home": 1.88,
      "lambda_away": 1.2149999999999999,
      "p1x2": {
        "home": 0.5292597671050385,
        "draw": 0.22508539913444894,
        "away": 0.24565483376051256
      },
      "ou25": {
        "over2_5": 0.597753585859201,
        "under2_5": 0.402246414140799
      },
      "btts": {
        "yes": 0.5959748924093233,
        "no": 0.40402510759067667
      },
      "dc": {
        "12": 0.7749146008655511,
        "1X": 0.7543451662394874,
        "X2": 0.4707402328949615
      },
      "dnb": {
        "home": 0.682991088971449,
        "away": 0.31700891102855094,
        "push": 0.22508539913444894
      },
      "team_ou15": {
        "home_over1_5": 0.560540495420165,
        "away_over1_5": 0.34278731833868964
      },
      "odds": {
        "status": "NO_VERIFIED_BOOKMAKER_QUOTE",
        "odds": null,
        "operator": null,
        "observed_timestamp": null
      },
      "market_no_vig": {
        "status": "NO_VALID_QUOTE",
        "market_no_vig": null
      },
      "edge": {
        "validated_edge": false,
        "edge_pp": null,
        "reason": "NO_VERIFIED_BOOKMAKER_QUOTE"
      },
      "classification": "FORECAST_ONLY",
      "settlement": "PENDING",
      "notes": "Roma vs Genoa; source https://nofluffpicks.com/match/roma-vs-genoa-2026-10-17; provenance NOFLUFFPICKS_SEASON_6_6; pre-match source snapshot viewed after cutoff before kickoff; inputs home xG=2.08 xGA=1.23 away xG=1.2 xGA=1.68; independent Poisson 0..19; Asian home -1 {\"win\":0.3020080299618936,\"push\":0.2272517371431451,\"lose\":0.47074023289496136}; no opponent-strength/home advantage calibration, sample heterogeneity, point-in-time vendor data not independently archived. No validated operator/time-stamped odds, no market-aware, corners, SOT, cards; no SHADOW/REAL. Schedules https://www.informador.mx/amp/deportes/futbol-hoy-en-vivo-calendario-de-partidos-del-17-de-octubre-de-2026-canales-horarios-streaming-20261016-0042.html ; https://www.skysports.com/football-scores-fixtures/2026-10-17"
    },
    {
      "record_id": "LEN17-TRO-LEN",
      "run_date": "2026-10-17",
      "record_type": "FREEZE_PROSPECTIVE",
      "fixture_key": "2026-10-17|TRO-LEN",
      "competition": "Ligue 1",
      "kickoff_cdmx": "2026-10-17 12:45 CDMX",
      "cutoff_cdmx": "2026-10-17T08:52:43-06:00",
      "freeze_cdmx": "2026-10-17T08:56:23-06:00",
      "model_version": "LENNON-PURE-GOALS-POISSON-V0.1-JS-REPRO",
      "features": {
        "home_xg": 1.41,
        "home_xga": 1.45,
        "away_xg": 1.85,
        "away_xga": 1.7
      },
      "lambda_home": 1.555,
      "lambda_away": 1.65,
      "p1x2": {
        "home": 0.3628312869759794,
        "draw": 0.23379119966836215,
        "away": 0.4033775133556585
      },
      "ou25": {
        "over2_5": 0.6211387928143653,
        "under2_5": 0.37886120718563465
      },
      "btts": {
        "yes": 0.6373196103761456,
        "no": 0.3626803896238544
      },
      "dc": {
        "12": 0.7662088003316379,
        "1X": 0.5966224866443415,
        "X2": 0.6371687130240207
      },
      "dnb": {
        "home": 0.4735410071235612,
        "away": 0.5264589928764389,
        "push": 0.23379119966836215
      },
      "team_ou15": {
        "home_over1_5": 0.4604111273523185,
        "away_over1_5": 0.4910677421550008
      },
      "odds": {
        "status": "NO_VERIFIED_BOOKMAKER_QUOTE",
        "odds": null,
        "operator": null,
        "observed_timestamp": null
      },
      "market_no_vig": {
        "status": "NO_VALID_QUOTE",
        "market_no_vig": null
      },
      "edge": {
        "validated_edge": false,
        "edge_pp": null,
        "reason": "NO_VERIFIED_BOOKMAKER_QUOTE"
      },
      "classification": "FORECAST_ONLY",
      "settlement": "PENDING",
      "notes": "Troyes vs Lens; source https://www.footboom1.com/uz/football/game/troyes-lens-2026-10-17; provenance FOOTBOOM_LAST10_MIXED; pre-match source snapshot viewed after cutoff before kickoff; inputs home xG=1.41 xGA=1.45 away xG=1.85 xGA=1.7; independent Poisson 0..19; Asian home -1 {\"win\":0.17582029694505188,\"push\":0.18701099003092753,\"lose\":0.6371687130240206}; no opponent-strength/home advantage calibration, sample heterogeneity, point-in-time vendor data not independently archived. No validated operator/time-stamped odds, no market-aware, corners, SOT, cards; no SHADOW/REAL. Schedules https://www.informador.mx/amp/deportes/futbol-hoy-en-vivo-calendario-de-partidos-del-17-de-octubre-de-2026-canales-horarios-streaming-20261016-0042.html ; https://www.skysports.com/football-scores-fixtures/2026-10-17"
    },
    {
      "record_id": "LEN17-LIL-BRE",
      "run_date": "2026-10-17",
      "record_type": "FREEZE_PROSPECTIVE",
      "fixture_key": "2026-10-17|LIL-BRE",
      "competition": "Ligue 1",
      "kickoff_cdmx": "2026-10-17 12:45 CDMX",
      "cutoff_cdmx": "2026-10-17T08:52:43-06:00",
      "freeze_cdmx": "2026-10-17T08:56:23-06:00",
      "model_version": "LENNON-PURE-GOALS-POISSON-V0.1-JS-REPRO",
      "features": {
        "home_xg": 1.38,
        "home_xga": 1.7,
        "away_xg": 2.22,
        "away_xga": 1.17
      },
      "lambda_home": 1.275,
      "lambda_away": 1.96,
      "p1x2": {
        "home": 0.24729849148333183,
        "draw": 0.21918630209598428,
        "away": 0.533515206420684
      },
      "ou25": {
        "over2_5": 0.627352831706472,
        "under2_5": 0.37264716829352795
      },
      "btts": {
        "yes": 0.6190708157976488,
        "no": 0.3809291842023512
      },
      "dc": {
        "12": 0.7808136979040158,
        "1X": 0.4664847935793161,
        "X2": 0.7527015085166682
      },
      "dnb": {
        "home": 0.3167189460778797,
        "away": 0.6832810539221202,
        "push": 0.21918630209598428
      },
      "team_ou15": {
        "home_over1_5": 0.3642945472962979,
        "away_over1_5": 0.5830590740736875
      },
      "odds": {
        "status": "NO_VERIFIED_BOOKMAKER_QUOTE",
        "odds": null,
        "operator": null,
        "observed_timestamp": null
      },
      "market_no_vig": {
        "status": "NO_VALID_QUOTE",
        "market_no_vig": null
      },
      "edge": {
        "validated_edge": false,
        "edge_pp": null,
        "reason": "NO_VERIFIED_BOOKMAKER_QUOTE"
      },
      "classification": "FORECAST_ONLY",
      "settlement": "PENDING",
      "notes": "Lille vs Brest; source https://www.tifolab.com/matches/1552786; provenance TIFOLAB_SEASON_6_6; pre-match source snapshot viewed after cutoff before kickoff; inputs home xG=1.38 xGA=1.7 away xG=2.22 xGA=1.17; independent Poisson 0..19; Asian home -1 {\"win\":0.10211374442557401,\"push\":0.14518474705775786,\"lose\":0.7527015085166682}; no opponent-strength/home advantage calibration, sample heterogeneity, point-in-time vendor data not independently archived. No validated operator/time-stamped odds, no market-aware, corners, SOT, cards; no SHADOW/REAL. Schedules https://www.informador.mx/amp/deportes/futbol-hoy-en-vivo-calendario-de-partidos-del-17-de-octubre-de-2026-canales-horarios-streaming-20261016-0042.html ; https://www.skysports.com/football-scores-fixtures/2026-10-17"
    },
    {
      "record_id": "LEN17-TEL-FEY",
      "run_date": "2026-10-17",
      "record_type": "FREEZE_PROSPECTIVE",
      "fixture_key": "2026-10-17|TEL-FEY",
      "competition": "Eredivisie",
      "kickoff_cdmx": "2026-10-17 12:00 CDMX",
      "cutoff_cdmx": "2026-10-17T08:52:43-06:00",
      "freeze_cdmx": "2026-10-17T08:56:23-06:00",
      "model_version": "LENNON-PURE-GOALS-POISSON-V0.1-JS-REPRO",
      "features": {
        "home_xg": 1.47,
        "home_xga": 1.68,
        "away_xg": 2.2,
        "away_xga": 0.91
      },
      "lambda_home": 1.19,
      "lambda_away": 1.94,
      "p1x2": {
        "home": 0.2314771100507616,
        "draw": 0.22020481694683167,
        "away": 0.5483180730024068
      },
      "ou25": {
        "over2_5": 0.605296053393386,
        "under2_5": 0.394703946606614
      },
      "btts": {
        "yes": 0.5957925834083402,
        "no": 0.4042074165916598
      },
      "dc": {
        "12": 0.7797951830531684,
        "1X": 0.45168192699759324,
        "X2": 0.7685228899492385
      },
      "dnb": {
        "home": 0.29684347259551985,
        "away": 0.7031565274044801,
        "push": 0.22020481694683167
      },
      "team_ou15": {
        "home_over1_5": 0.3337554316939182,
        "away_over1_5": 0.5775103876535376
      },
      "odds": {
        "status": "NO_VERIFIED_BOOKMAKER_QUOTE",
        "odds": null,
        "operator": null,
        "observed_timestamp": null
      },
      "market_no_vig": {
        "status": "NO_VALID_QUOTE",
        "market_no_vig": null
      },
      "edge": {
        "validated_edge": false,
        "edge_pp": null,
        "reason": "NO_VERIFIED_BOOKMAKER_QUOTE"
      },
      "classification": "FORECAST_ONLY",
      "settlement": "PENDING",
      "notes": "Telstar vs Feyenoord; source https://www.footboom1.com/it/football/game/telstar-feyenoord-2026-10-17; provenance FOOTBOOM_LAST10_MIXED; pre-match source snapshot viewed after cutoff before kickoff; inputs home xG=1.47 xGA=1.68 away xG=2.2 xGA=0.91; independent Poisson 0..19; Asian home -1 {\"win\":0.09129557362431741,\"push\":0.14018153642644415,\"lose\":0.7685228899492385}; no opponent-strength/home advantage calibration, sample heterogeneity, point-in-time vendor data not independently archived. No validated operator/time-stamped odds, no market-aware, corners, SOT, cards; no SHADOW/REAL. Schedules https://www.informador.mx/amp/deportes/futbol-hoy-en-vivo-calendario-de-partidos-del-17-de-octubre-de-2026-canales-horarios-streaming-20261016-0042.html ; https://www.skysports.com/football-scores-fixtures/2026-10-17"
    },
    {
      "record_id": "LEN17-PHI-CLT",
      "run_date": "2026-10-17",
      "record_type": "FREEZE_PROSPECTIVE",
      "fixture_key": "2026-10-17|PHI-CLT",
      "competition": "MLS",
      "kickoff_cdmx": "2026-10-17 12:30 CDMX",
      "cutoff_cdmx": "2026-10-17T08:52:43-06:00",
      "freeze_cdmx": "2026-10-17T08:56:23-06:00",
      "model_version": "LENNON-PURE-GOALS-POISSON-V0.1-JS-REPRO",
      "features": {
        "home_xg": 2.42,
        "home_xga": 1.16,
        "away_xg": 1.55,
        "away_xga": 1.85
      },
      "lambda_home": 2.135,
      "lambda_away": 1.355,
      "p1x2": {
        "home": 0.5531819385516608,
        "draw": 0.20724043848718796,
        "away": 0.23957762296115134
      },
      "ou25": {
        "over2_5": 0.6772992473848422,
        "under2_5": 0.32270075261515785
      },
      "btts": {
        "yes": 0.6543089873427375,
        "no": 0.34569101265726254
      },
      "dc": {
        "12": 0.7927595615128121,
        "1X": 0.7604223770388487,
        "X2": 0.4468180614483393
      },
      "dnb": {
        "home": 0.6977928307746062,
        "away": 0.3022071692253937,
        "push": 0.20724043848718796
      },
      "team_ou15": {
        "home_over1_5": 0.6293032091691697,
        "away_over1_5": 0.39253412156595086
      },
      "odds": {
        "status": "NO_VERIFIED_BOOKMAKER_QUOTE",
        "odds": null,
        "operator": null,
        "observed_timestamp": null
      },
      "market_no_vig": {
        "status": "NO_VALID_QUOTE",
        "market_no_vig": null
      },
      "edge": {
        "validated_edge": false,
        "edge_pp": null,
        "reason": "NO_VERIFIED_BOOKMAKER_QUOTE"
      },
      "classification": "FORECAST_ONLY",
      "settlement": "PENDING",
      "notes": "Philadelphia Union vs Charlotte; source https://www.footboom1.com/br/football/game/philadelphia-union-charlotte-2026-10-17; provenance FOOTBOOM_LAST10_MIXED; pre-match source snapshot viewed after cutoff before kickoff; inputs home xG=2.42 xGA=1.16 away xG=1.55 xGA=1.85; independent Poisson 0..19; Asian home -1 {\"win\":0.3357583603303854,\"push\":0.21742357822127534,\"lose\":0.44681806144833924}; no opponent-strength/home advantage calibration, sample heterogeneity, point-in-time vendor data not independently archived. No validated operator/time-stamped odds, no market-aware, corners, SOT, cards; no SHADOW/REAL. Schedules https://www.informador.mx/amp/deportes/futbol-hoy-en-vivo-calendario-de-partidos-del-17-de-octubre-de-2026-canales-horarios-streaming-20261016-0042.html ; https://www.skysports.com/football-scores-fixtures/2026-10-17"
    },
    {
      "record_id": "LEN17-MIN-STL",
      "run_date": "2026-10-17",
      "record_type": "FREEZE_PROSPECTIVE",
      "fixture_key": "2026-10-17|MIN-STL",
      "competition": "MLS",
      "kickoff_cdmx": "2026-10-17 14:30 CDMX",
      "cutoff_cdmx": "2026-10-17T08:52:43-06:00",
      "freeze_cdmx": "2026-10-17T08:56:23-06:00",
      "model_version": "LENNON-PURE-GOALS-POISSON-V0.1-JS-REPRO",
      "features": {
        "home_xg": 1.7,
        "home_xga": 1.59,
        "away_xg": 1.62,
        "away_xga": 1.16
      },
      "lambda_home": 1.43,
      "lambda_away": 1.605,
      "p1x2": {
        "home": 0.3415537430574282,
        "draw": 0.24041227866405854,
        "away": 0.41803397827851335
      },
      "ou25": {
        "over2_5": 0.5846054670238452,
        "under2_5": 0.4153945329761548
      },
      "btts": {
        "yes": 0.6078761857216077,
        "no": 0.39212381427839227
      },
      "dc": {
        "12": 0.7595877213359415,
        "1X": 0.5819660217214867,
        "X2": 0.6584462569425719
      },
      "dnb": {
        "home": 0.4496567459736093,
        "away": 0.5503432540263907,
        "push": 0.24041227866405854
      },
      "team_ou15": {
        "home_over1_5": 0.4184793189476765,
        "away_over1_5": 0.47668270945884506
      },
      "odds": {
        "status": "NO_VERIFIED_BOOKMAKER_QUOTE",
        "odds": null,
        "operator": null,
        "observed_timestamp": null
      },
      "market_no_vig": {
        "status": "NO_VALID_QUOTE",
        "market_no_vig": null
      },
      "edge": {
        "validated_edge": false,
        "edge_pp": null,
        "reason": "NO_VERIFIED_BOOKMAKER_QUOTE"
      },
      "classification": "FORECAST_ONLY",
      "settlement": "PENDING",
      "notes": "Minnesota United vs St Louis City; source https://www.tifolab.com/matches/1490542; provenance TIFOLAB_SEASON_29_29; pre-match source snapshot viewed after cutoff before kickoff; inputs home xG=1.7 xGA=1.59 away xG=1.62 xGA=1.16; independent Poisson 0..19; Asian home -1 {\"win\":0.15724882031625062,\"push\":0.18430492274117777,\"lose\":0.6584462569425715}; no opponent-strength/home advantage calibration, sample heterogeneity, point-in-time vendor data not independently archived. No validated operator/time-stamped odds, no market-aware, corners, SOT, cards; no SHADOW/REAL. Schedules https://www.informador.mx/amp/deportes/futbol-hoy-en-vivo-calendario-de-partidos-del-17-de-octubre-de-2026-canales-horarios-streaming-20261016-0042.html ; https://www.skysports.com/football-scores-fixtures/2026-10-17"
    }
  ]
}
```
