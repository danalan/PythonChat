# LENNON prospective freeze — 16 Oct 2026

**Run ID** LENNON-2026-10-16-PREDICTION-FIRST. **Pre-research cutoff** 2026-10-16T08:43:16-06:00 CDMX. **Prospective freeze** 2026-10-16T08:45:09-06:00 CDMX, prior to all 8 listed kickoffs. **REAL=0, SHADOW=0, parlays=0.**

Canonical CP: `LENNON Prediction Ledger!A208:AE215`, write and readback verified. 17 previous UEFA forecasts settled first in CP rows 191–207. Source of schedules: https://www.theguardian.com/football/fixtures/2026/Oct/16 ; Liga MX https://en.as.com/resultados/futbol/mexico_apertura/ .

**Executed engine:** LENNON PURE independent Poisson V0.1, same formula as `exp003_recovery/LENNON_PURE_GOALS_POISSON_REPRO_V0_1.mjs`: lambdaH=(home xG+away xGA)/2, lambdaA=(away xG+home xGA)/2, scores 0..19. No market odds enter p_model. Outputs 1X2, DC, DNB, home Asian -1 with win/push/lose, O/U 2.5, BTTS, team O/U 1.5. MARKET-AWARE, Corners, Team Shots/SOT and Cards engines **NOT EXECUTED**. Player props/fouls/offsides/throw-ins/goal kicks research-only.

| Fixture | League | Kickoff CDMX | λH/λA | P(1/X/2)% | Classification |
|---|---|---|---|---|---|
| 2026-10-16|FRA-KOL | Bundesliga | 2026-10-16 12:30 CDMX | 1.775/1.665 | 41.0/22.5/36.5 | FORECAST_ONLY |
| 2026-10-16|FRO-SAS | Serie A | 2026-10-16 12:45 CDMX | 1.725/1.920 | 35.2/21.7/43.1 | FORECAST_ONLY |
| 2026-10-16|BUR-WOL | EFL Championship | 2026-10-16 13:00 CDMX | 1.380/1.575 | 33.5/24.4/42.1 | FORECAST_ONLY |
| 2026-10-16|DEP-LEV | La Liga | 2026-10-16 13:00 CDMX | 1.540/1.405 | 40.7/24.5/34.8 | FORECAST_ONLY |
| 2026-10-16|AYR-PAR | Scottish Championship | 2026-10-16 12:30 CDMX | 0.875/1.540 | 21.4/25.7/52.9 | FORECAST_ONLY |
| 2026-10-16|NEC-ATL | Liga MX | 2026-10-16 19:00 CDMX | 1.545/1.620 | 36.6/23.6/39.8 | FORECAST_ONLY |
| 2026-10-16|ATL-PUM | Liga MX | 2026-10-16 21:00 CDMX | 1.575/1.505 | 39.6/23.9/36.5 | FORECAST_ONLY |
| 2026-10-16|TIJ-PUE | Liga MX | 2026-10-16 21:05 CDMX | 1.460/1.525 | 36.4/24.4/39.3 | FORECAST_ONLY |

**Provenance / limitations:** FootyStats 2026/27 pre-match xG/xGA overall, 5–11 sample matches depending on team; Frankfurt uses last-ten/mixed competition inputs. Data pages retrieved after pre-research cutoff but before kickoff. Individual source URLs, input sample sizes, market prices when observed and full-precision outputs below. Observed quotes have unverified bookmaker/publication timestamp; no actionable EV, CLV or SHADOW edge. No-vig comparisons are diagnostics only. Unadjusted for lineups, injuries, opponent strength, home advantage or league-level distortions. One additional identified major fixture Le Mans–Toulouse excluded due incomplete independently verified team xGA; no exhaustive global league coverage claimed.

**Full-precision CP mirror (JSON, frozen as recorded):**

```json
{
  "run_id": "LENNON-2026-10-16-PREDICTION-FIRST",
  "cutoff": "2026-10-16T08:43:16-06:00",
  "freeze": "2026-10-16T08:45:09-06:00",
  "real": 0,
  "shadow": 0,
  "forecasts": [
    {
      "record_id": "LEN16-FRA-KOL",
      "run_date": "2026-10-16",
      "record_type": "FREEZE_PROSPECTIVE",
      "fixture_key": "2026-10-16|FRA-KOL",
      "competition": "Bundesliga",
      "kickoff_cdmx": "2026-10-16 12:30 CDMX",
      "cutoff_cdmx": "2026-10-16T08:43:16-06:00",
      "freeze_cdmx": "2026-10-16T08:45:09-06:00",
      "model_version": "LENNON-PURE-GOALS-POISSON-V0.1-JS-REPRO",
      "features": {
        "home_xg": 2.16,
        "home_xga": 1.68,
        "away_xg": 1.65,
        "away_xga": 1.39,
        "lambda_home": 1.775,
        "lambda_away": 1.665
      },
      "p_model": {
        "result_1x2": {
          "home": 0.41041666187877923,
          "draw": 0.22462684125129045,
          "away": 0.36495649686993037
        },
        "over_under_2_5": {
          "over2_5": 0.6679124669964094,
          "under2_5": 0.3320875330035906
        },
        "btts": {
          "yes": 0.6733905778464081,
          "no": 0.3266094221535919
        },
        "double_chance": {
          "12": 0.7753731587487096,
          "1X": 0.6350435031300696,
          "X2": 0.5895833381212208
        },
        "draw_no_bet": {
          "home": 0.5293150236733833,
          "away": 0.47068497632661666,
          "push": 0.22462684125129045
        },
        "team_goals_over_1_5": {
          "home_over1_5": 0.5296834276389677,
          "away_over1_5": 0.4958068964780167
        }
      },
      "observed_market": {
        "home": 1.8333333333,
        "draw": 4,
        "away": 3.55,
        "status": "AGGREGATOR_DIAGNOSTIC_NOT_EXECUTABLE",
        "bookmaker_timestamp_verified": false
      },
      "market_no_vig": {
        "home": 0.5063893016390172,
        "draw": 0.23209509658032965,
        "away": 0.26151560178065314
      },
      "diagnostic_difference_pp": {
        "home": -9.597263976023795,
        "draw": -0.7468255329039192,
        "away": 10.344089508927723,
        "status": "DIAGNOSTIC_NOT_VALIDATED_EDGE"
      },
      "classification": "FORECAST_ONLY",
      "result": "PENDING",
      "provenance": "Eintracht Frankfurt vs FC Köln; xG/xGA overall FootyStats pre-match 2026/27 10/10 last10 mixed, retrieved after pre-research cutoff and before kickoff; https://footystats.org/germany/1-fc-koln-vs-eintracht-frankfurt-h2h-stats; fixture schedule Guardian https://www.theguardian.com/football/fixtures/2026/Oct/16 and LigaMX https://en.as.com/resultados/futbol/mexico_apertura/; independent Poisson n=0..19, lambdaH=(home xG+away xGA)/2, lambdaA=(away xG+home xGA)/2; Asian home -1 {\"win\":0.21610439551564672,\"push\":0.19431226636313248,\"lose\":0.5895833381212208}; input sources not timestamped point-in-time, not calibrated or market-aware. StatMuse +120? market +FRA -120/+300/+255 https://www.statmuse.com/fc/match/-113188; decimal conversion; bookmaker/timestamp unknown NO validated bookmaker timestamp, NO SHADOW/REAL. Corners/Shots/SOT/Cards NOT EXECUTED."
    },
    {
      "record_id": "LEN16-FRO-SAS",
      "run_date": "2026-10-16",
      "record_type": "FREEZE_PROSPECTIVE",
      "fixture_key": "2026-10-16|FRO-SAS",
      "competition": "Serie A",
      "kickoff_cdmx": "2026-10-16 12:45 CDMX",
      "cutoff_cdmx": "2026-10-16T08:43:16-06:00",
      "freeze_cdmx": "2026-10-16T08:45:09-06:00",
      "model_version": "LENNON-PURE-GOALS-POISSON-V0.1-JS-REPRO",
      "features": {
        "home_xg": 1.75,
        "home_xga": 2.05,
        "away_xg": 1.79,
        "away_xga": 1.7,
        "lambda_home": 1.725,
        "lambda_away": 1.92
      },
      "p_model": {
        "result_1x2": {
          "home": 0.3523522018290461,
          "draw": 0.2168813228795107,
          "away": 0.43076647529144324
        },
        "over_under_2_5": {
          "over2_5": 0.7051411990513371,
          "under2_5": 0.2948588009486629
        },
        "btts": {
          "yes": 0.701341395950665,
          "no": 0.298658604049335
        },
        "double_chance": {
          "12": 0.7831186771204893,
          "1X": 0.5692335247085568,
          "X2": 0.647647798170954
        },
        "draw_no_bet": {
          "home": 0.4499346167105063,
          "away": 0.5500653832894937,
          "push": 0.2168813228795107
        },
        "team_goals_over_1_5": {
          "home_over1_5": 0.5144784339188494,
          "away_over1_5": 0.5719076705793641
        }
      },
      "observed_market": {
        "home": 2.49,
        "draw": 3.56,
        "away": 2.86,
        "status": "AGGREGATOR_DIAGNOSTIC_NOT_EXECUTABLE",
        "bookmaker_timestamp_verified": false
      },
      "market_no_vig": {
        "home": 0.3890948279156507,
        "draw": 0.27214778694100294,
        "away": 0.3387573851433463
      },
      "diagnostic_difference_pp": {
        "home": -3.6742626086604613,
        "draw": -5.526646406149224,
        "away": 9.200909014809694,
        "status": "DIAGNOSTIC_NOT_VALIDATED_EDGE"
      },
      "classification": "FORECAST_ONLY",
      "result": "PENDING",
      "provenance": "Frosinone vs Sassuolo; xG/xGA overall FootyStats pre-match 2026/27 6/6 season, retrieved after pre-research cutoff and before kickoff; https://footystats.org/italy/us-sassuolo-calcio-vs-frosinone-calcio-h2h-stats; fixture schedule Guardian https://www.theguardian.com/football/fixtures/2026/Oct/16 and LigaMX https://en.as.com/resultados/futbol/mexico_apertura/; independent Poisson n=0..19, lambdaH=(home xG+away xGA)/2, lambdaA=(away xG+home xGA)/2; Asian home -1 {\"win\":0.1780088903368596,\"push\":0.17434331149218643,\"lose\":0.6476477981709541}; input sources not timestamped point-in-time, not calibrated or market-aware. StatsBet listing Pinnacle, no bookmaker publication timestamp https://statsbet.org/football/matches/frosinone-vs-sassuolo-2026-10-16 NO validated bookmaker timestamp, NO SHADOW/REAL. Corners/Shots/SOT/Cards NOT EXECUTED."
    },
    {
      "record_id": "LEN16-BUR-WOL",
      "run_date": "2026-10-16",
      "record_type": "FREEZE_PROSPECTIVE",
      "fixture_key": "2026-10-16|BUR-WOL",
      "competition": "EFL Championship",
      "kickoff_cdmx": "2026-10-16 13:00 CDMX",
      "cutoff_cdmx": "2026-10-16T08:43:16-06:00",
      "freeze_cdmx": "2026-10-16T08:45:09-06:00",
      "model_version": "LENNON-PURE-GOALS-POISSON-V0.1-JS-REPRO",
      "features": {
        "home_xg": 1.47,
        "home_xga": 1.52,
        "away_xg": 1.63,
        "away_xga": 1.29,
        "lambda_home": 1.38,
        "lambda_away": 1.575
      },
      "p_model": {
        "result_1x2": {
          "home": 0.33497277032673195,
          "draw": 0.24383590705415925,
          "away": 0.4211913226191087
        },
        "over_under_2_5": {
          "over2_5": 0.5666528143641316,
          "under2_5": 0.4333471856358684
        },
        "btts": {
          "yes": 0.5934925548350561,
          "no": 0.40650744516494386
        },
        "double_chance": {
          "12": 0.7561640929458406,
          "1X": 0.5788086773808911,
          "X2": 0.665027229673268
        },
        "draw_no_bet": {
          "home": 0.44298952231618854,
          "away": 0.5570104776838114,
          "push": 0.24383590705415925
        },
        "team_goals_over_1_5": {
          "home_over1_5": 0.40124304371777914,
          "away_over1_5": 0.46695555184603116
        }
      },
      "observed_market": {
        "home": 2.85,
        "draw": 3.5,
        "away": 2.35,
        "status": "AGGREGATOR_DIAGNOSTIC_NOT_EXECUTABLE",
        "bookmaker_timestamp_verified": false
      },
      "market_no_vig": {
        "home": 0.33035445325835927,
        "draw": 0.26900291193894965,
        "away": 0.400642634802691
      },
      "diagnostic_difference_pp": {
        "home": 0.46183170683726793,
        "draw": -2.51670048847904,
        "away": 2.0548687816417663,
        "status": "DIAGNOSTIC_NOT_VALIDATED_EDGE"
      },
      "classification": "FORECAST_ONLY",
      "result": "PENDING",
      "provenance": "Burnley vs Wolverhampton; xG/xGA overall FootyStats pre-match 2026/27 10/9 season, retrieved after pre-research cutoff and before kickoff; https://footystats.org/es/international/burnley-fc-vs-wolverhampton-wanderers-fc-h2h-stats; fixture schedule Guardian https://www.theguardian.com/football/fixtures/2026/Oct/16 and LigaMX https://en.as.com/resultados/futbol/mexico_apertura/; independent Poisson n=0..19, lambdaH=(home xG+away xGA)/2, lambdaA=(away xG+home xGA)/2; Asian home -1 {\"win\":0.1509842298469122,\"push\":0.18398854047982044,\"lose\":0.6650272296732673}; input sources not timestamped point-in-time, not calibrated or market-aware. FootyStats aggregated page; operator and publication timestamp unknown NO validated bookmaker timestamp, NO SHADOW/REAL. Corners/Shots/SOT/Cards NOT EXECUTED."
    },
    {
      "record_id": "LEN16-DEP-LEV",
      "run_date": "2026-10-16",
      "record_type": "FREEZE_PROSPECTIVE",
      "fixture_key": "2026-10-16|DEP-LEV",
      "competition": "La Liga",
      "kickoff_cdmx": "2026-10-16 13:00 CDMX",
      "cutoff_cdmx": "2026-10-16T08:43:16-06:00",
      "freeze_cdmx": "2026-10-16T08:45:09-06:00",
      "model_version": "LENNON-PURE-GOALS-POISSON-V0.1-JS-REPRO",
      "features": {
        "home_xg": 1.33,
        "home_xga": 1.48,
        "away_xg": 1.33,
        "away_xga": 1.75,
        "lambda_home": 1.54,
        "lambda_away": 1.405
      },
      "p_model": {
        "result_1x2": {
          "home": 0.4074287000308202,
          "draw": 0.24496924576726017,
          "away": 0.34760205420191975
        },
        "over_under_2_5": {
          "over2_5": 0.5643753841057803,
          "under2_5": 0.43562461589421975
        },
        "btts": {
          "yes": 0.5928539019363696,
          "no": 0.40714609806363045
        },
        "double_chance": {
          "12": 0.7550307542327399,
          "1X": 0.6523979457980804,
          "X2": 0.5925712999691799
        },
        "draw_no_bet": {
          "home": 0.5396186814202663,
          "away": 0.46038131857973386,
          "push": 0.24496924576726017
        },
        "team_goals_over_1_5": {
          "home_over1_5": 0.45547200237547564,
          "away_over1_5": 0.40989222923071206
        }
      },
      "observed_market": {
        "status": "NOT_OBSERVED"
      },
      "market_no_vig": null,
      "diagnostic_difference_pp": null,
      "classification": "FORECAST_ONLY",
      "result": "PENDING",
      "provenance": "Deportivo La Coruña vs Levante; xG/xGA overall FootyStats pre-match 2026/27 8/7 season, retrieved after pre-research cutoff and before kickoff; https://footystats.org/spain/real-club-deportivo-de-la-coruna-vs-levante-ud-h2h-stats; fixture schedule Guardian https://www.theguardian.com/football/fixtures/2026/Oct/16 and LigaMX https://en.as.com/resultados/futbol/mexico_apertura/; independent Poisson n=0..19, lambdaH=(home xG+away xGA)/2, lambdaA=(away xG+home xGA)/2; Asian home -1 {\"win\":0.2008186223379879,\"push\":0.2066100776928321,\"lose\":0.5925712999691799}; input sources not timestamped point-in-time, not calibrated or market-aware. No price observed. NO validated bookmaker timestamp, NO SHADOW/REAL. Corners/Shots/SOT/Cards NOT EXECUTED."
    },
    {
      "record_id": "LEN16-AYR-PAR",
      "run_date": "2026-10-16",
      "record_type": "FREEZE_PROSPECTIVE",
      "fixture_key": "2026-10-16|AYR-PAR",
      "competition": "Scottish Championship",
      "kickoff_cdmx": "2026-10-16 12:30 CDMX",
      "cutoff_cdmx": "2026-10-16T08:43:16-06:00",
      "freeze_cdmx": "2026-10-16T08:45:09-06:00",
      "model_version": "LENNON-PURE-GOALS-POISSON-V0.1-JS-REPRO",
      "features": {
        "home_xg": 0.98,
        "home_xga": 1.48,
        "away_xg": 1.6,
        "away_xga": 0.77,
        "lambda_home": 0.875,
        "lambda_away": 1.54
      },
      "p_model": {
        "result_1x2": {
          "home": 0.21377010252759518,
          "draw": 0.2569711472523223,
          "away": 0.5292587502200826
        },
        "over_under_2_5": {
          "over2_5": 0.4342053234607516,
          "under2_5": 0.5657946765392484
        },
        "btts": {
          "yes": 0.45812421781626683,
          "no": 0.5418757821837332
        },
        "double_chance": {
          "12": 0.7430288527476778,
          "1X": 0.4707412497799175,
          "X2": 0.7862298974724049
        },
        "draw_no_bet": {
          "home": 0.28770094423263065,
          "away": 0.7122990557673693,
          "push": 0.2569711472523223
        },
        "team_goals_over_1_5": {
          "home_over1_5": 0.2183837131027967,
          "away_over1_5": 0.45547200237547575
        }
      },
      "observed_market": {
        "status": "NOT_OBSERVED"
      },
      "market_no_vig": null,
      "diagnostic_difference_pp": null,
      "classification": "FORECAST_ONLY",
      "result": "PENDING",
      "provenance": "Ayr United vs Partick Thistle; xG/xGA overall FootyStats pre-match 2026/27 10/9 season, retrieved after pre-research cutoff and before kickoff; https://footystats.org/scotland/partick-thistle-fc-vs-ayr-united-fc-h2h-stats; fixture schedule Guardian https://www.theguardian.com/football/fixtures/2026/Oct/16 and LigaMX https://en.as.com/resultados/futbol/mexico_apertura/; independent Poisson n=0..19, lambdaH=(home xG+away xGA)/2, lambdaA=(away xG+home xGA)/2; Asian home -1 {\"win\":0.06963438400088616,\"push\":0.1441357185267091,\"lose\":0.7862298974724047}; input sources not timestamped point-in-time, not calibrated or market-aware. No price observed. NO validated bookmaker timestamp, NO SHADOW/REAL. Corners/Shots/SOT/Cards NOT EXECUTED."
    },
    {
      "record_id": "LEN16-NEC-ATL",
      "run_date": "2026-10-16",
      "record_type": "FREEZE_PROSPECTIVE",
      "fixture_key": "2026-10-16|NEC-ATL",
      "competition": "Liga MX",
      "kickoff_cdmx": "2026-10-16 19:00 CDMX",
      "cutoff_cdmx": "2026-10-16T08:43:16-06:00",
      "freeze_cdmx": "2026-10-16T08:45:09-06:00",
      "model_version": "LENNON-PURE-GOALS-POISSON-V0.1-JS-REPRO",
      "features": {
        "home_xg": 1.56,
        "home_xga": 1.86,
        "away_xg": 1.38,
        "away_xga": 1.53,
        "lambda_home": 1.545,
        "lambda_away": 1.62
      },
      "p_model": {
        "result_1x2": {
          "home": 0.36612403446506964,
          "draw": 0.23555574108675562,
          "away": 0.3983202244481747
        },
        "over_under_2_5": {
          "over2_5": 0.6127438209773398,
          "under2_5": 0.3872561790226602
        },
        "btts": {
          "yes": 0.6310035715075762,
          "no": 0.36899642849242376
        },
        "double_chance": {
          "12": 0.7644442589132443,
          "1X": 0.6016797755518253,
          "X2": 0.6338759655349303
        },
        "draw_no_bet": {
          "home": 0.4789414403943094,
          "away": 0.5210585596056907,
          "push": 0.23555574108675562
        },
        "team_goals_over_1_5": {
          "home_over1_5": 0.45712128773768035,
          "away_over1_5": 0.48150540840092876
        }
      },
      "observed_market": {
        "home": 2.44,
        "draw": 3.46,
        "away": 2.58,
        "status": "AGGREGATOR_DIAGNOSTIC_NOT_EXECUTABLE",
        "bookmaker_timestamp_verified": false
      },
      "market_no_vig": {
        "home": 0.3772248609726002,
        "draw": 0.266019844154088,
        "away": 0.35675529487331176
      },
      "diagnostic_difference_pp": {
        "home": -1.1100826507530581,
        "draw": -3.046410306733241,
        "away": 4.1564929574862965,
        "status": "DIAGNOSTIC_NOT_VALIDATED_EDGE"
      },
      "classification": "FORECAST_ONLY",
      "result": "PENDING",
      "provenance": "Necaxa vs Atlas; xG/xGA overall FootyStats pre-match 2026/27 11/11 season, retrieved after pre-research cutoff and before kickoff; https://footystats.org/mexico/csyd-atlas-de-guadalajara-vs-club-necaxa-h2h-stats; fixture schedule Guardian https://www.theguardian.com/football/fixtures/2026/Oct/16 and LigaMX https://en.as.com/resultados/futbol/mexico_apertura/; independent Poisson n=0..19, lambdaH=(home xG+away xGA)/2, lambdaA=(away xG+home xGA)/2; Asian home -1 {\"win\":0.17716544027623926,\"push\":0.18895859418883004,\"lose\":0.6338759655349306}; input sources not timestamped point-in-time, not calibrated or market-aware. FootyStats Liga MX odds board https://footystats.org/es/mexico/liga-mx/odds; bookmaker/time unknown NO validated bookmaker timestamp, NO SHADOW/REAL. Corners/Shots/SOT/Cards NOT EXECUTED."
    },
    {
      "record_id": "LEN16-ATL-PUM",
      "run_date": "2026-10-16",
      "record_type": "FREEZE_PROSPECTIVE",
      "fixture_key": "2026-10-16|ATL-PUM",
      "competition": "Liga MX",
      "kickoff_cdmx": "2026-10-16 21:00 CDMX",
      "cutoff_cdmx": "2026-10-16T08:43:16-06:00",
      "freeze_cdmx": "2026-10-16T08:45:09-06:00",
      "model_version": "LENNON-PURE-GOALS-POISSON-V0.1-JS-REPRO",
      "features": {
        "home_xg": 1.58,
        "home_xga": 1.62,
        "away_xg": 1.39,
        "away_xga": 1.57,
        "lambda_home": 1.575,
        "lambda_away": 1.505
      },
      "p_model": {
        "result_1x2": {
          "home": 0.3955931866607671,
          "draw": 0.23923463404253403,
          "away": 0.3651721792966988
        },
        "over_under_2_5": {
          "over2_5": 0.5944922867341527,
          "under2_5": 0.40550771326584734
        },
        "btts": {
          "yes": 0.6169344101359421,
          "no": 0.3830655898640579
        },
        "double_chance": {
          "12": 0.7607653659574659,
          "1X": 0.6348278207033011,
          "X2": 0.6044068133392329
        },
        "draw_no_bet": {
          "home": 0.5199936857836461,
          "away": 0.48000631421635387,
          "push": 0.23923463404253403
        },
        "team_goals_over_1_5": {
          "home_over1_5": 0.4669555518460315,
          "away_over1_5": 0.44384667895096647
        }
      },
      "observed_market": {
        "home": 2.27,
        "draw": 3.46,
        "away": 2.85,
        "status": "AGGREGATOR_DIAGNOSTIC_NOT_EXECUTABLE",
        "bookmaker_timestamp_verified": false
      },
      "market_no_vig": {
        "home": 0.4077371230571394,
        "draw": 0.2675038350692793,
        "away": 0.3247590418735812
      },
      "diagnostic_difference_pp": {
        "home": -1.214393639637229,
        "draw": -2.8269201026745296,
        "away": 4.041313742311764,
        "status": "DIAGNOSTIC_NOT_VALIDATED_EDGE"
      },
      "classification": "FORECAST_ONLY",
      "result": "PENDING",
      "provenance": "Atlante vs Pumas UNAM; xG/xGA overall FootyStats pre-match 2026/27 11/11 season, retrieved after pre-research cutoff and before kickoff; https://footystats.org/mexico/club-universidad-nacional-vs-club-atlante-h2h-stats; fixture schedule Guardian https://www.theguardian.com/football/fixtures/2026/Oct/16 and LigaMX https://en.as.com/resultados/futbol/mexico_apertura/; independent Poisson n=0..19, lambdaH=(home xG+away xGA)/2, lambdaA=(away xG+home xGA)/2; Asian home -1 {\"win\":0.19596913132987648,\"push\":0.19962405533089078,\"lose\":0.6044068133392327}; input sources not timestamped point-in-time, not calibrated or market-aware. FootyStats Liga MX odds board https://footystats.org/es/mexico/liga-mx/odds; bookmaker/time unknown NO validated bookmaker timestamp, NO SHADOW/REAL. Corners/Shots/SOT/Cards NOT EXECUTED."
    },
    {
      "record_id": "LEN16-TIJ-PUE",
      "run_date": "2026-10-16",
      "record_type": "FREEZE_PROSPECTIVE",
      "fixture_key": "2026-10-16|TIJ-PUE",
      "competition": "Liga MX",
      "kickoff_cdmx": "2026-10-16 21:05 CDMX",
      "cutoff_cdmx": "2026-10-16T08:43:16-06:00",
      "freeze_cdmx": "2026-10-16T08:45:09-06:00",
      "model_version": "LENNON-PURE-GOALS-POISSON-V0.1-JS-REPRO",
      "features": {
        "home_xg": 1.31,
        "home_xga": 1.62,
        "away_xg": 1.43,
        "away_xga": 1.61,
        "lambda_home": 1.46,
        "lambda_away": 1.525
      },
      "p_model": {
        "result_1x2": {
          "home": 0.3638976451351446,
          "draw": 0.24355650726323252,
          "away": 0.39254584760162287
        },
        "over_under_2_5": {
          "over2_5": 0.5734409043511539,
          "under2_5": 0.4265590956488461
        },
        "btts": {
          "yes": 0.6006821719541429,
          "no": 0.39931782804585714
        },
        "double_chance": {
          "12": 0.7564434927367675,
          "1X": 0.6074541523983772,
          "X2": 0.6361023548648554
        },
        "draw_no_bet": {
          "home": 0.4810638846512971,
          "away": 0.5189361153487029,
          "push": 0.24355650726323252
        },
        "team_goals_over_1_5": {
          "home_over1_5": 0.428698764164793,
          "away_over1_5": 0.4505068314152867
        }
      },
      "observed_market": {
        "home": 1.83,
        "draw": 3.68,
        "away": 3.83,
        "status": "AGGREGATOR_DIAGNOSTIC_NOT_EXECUTABLE",
        "bookmaker_timestamp_verified": false
      },
      "market_no_vig": {
        "home": 0.5063061962733991,
        "draw": 0.2517772660816088,
        "away": 0.24191653764499224
      },
      "diagnostic_difference_pp": {
        "home": -14.240855113825452,
        "draw": -0.822075881837625,
        "away": 15.062930995663063,
        "status": "DIAGNOSTIC_NOT_VALIDATED_EDGE"
      },
      "classification": "FORECAST_ONLY",
      "result": "PENDING",
      "provenance": "Tijuana vs Puebla; xG/xGA overall FootyStats pre-match 2026/27 10/11 season, retrieved after pre-research cutoff and before kickoff; https://footystats.org/mexico/club-tijuana-xoloitzcuintles-de-caliente-vs-puebla-fc-h2h-stats; fixture schedule Guardian https://www.theguardian.com/football/fixtures/2026/Oct/16 and LigaMX https://en.as.com/resultados/futbol/mexico_apertura/; independent Poisson n=0..19, lambdaH=(home xG+away xGA)/2, lambdaA=(away xG+home xGA)/2; Asian home -1 {\"win\":0.17114885051408343,\"push\":0.19274879462106115,\"lose\":0.6361023548648554}; input sources not timestamped point-in-time, not calibrated or market-aware. FootyStats Liga MX odds board https://footystats.org/es/mexico/liga-mx/odds; bookmaker/time unknown NO validated bookmaker timestamp, NO SHADOW/REAL. Corners/Shots/SOT/Cards NOT EXECUTED."
    }
  ]
}
```

No retrofreeze or silent rewriting of previous records.