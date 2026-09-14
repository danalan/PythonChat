"""Economic pricing proxy for EXP-003 historical replay.

MARKET_PROXY_V1 is intentionally independent from p_model. It uses only
pre-ticket 1X2 market odds:
1) proportional de-vig of 1X2;
2) fit independent-Poisson home/away lambdas to the de-vigged 1X2 vector;
3) derive a score-based target-market fair probability;
4) re-apply the source 1X2 overround proportionally to obtain a synthetic
   executable-price proxy.

The resulting odds are NOT claimed to be historical Caliente odds. Exact
archived target-market prices, when available, belong in a separate audit.
"""
from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Iterable

import numpy as np
from scipy.optimize import minimize


@dataclass(frozen=True)
class ProxyPrice:
    market: str
    source_odds_1x2: tuple[float, float, float]
    source_overround: float
    fair_probability: float
    fair_decimal: float
    proxy_decimal: float
    lambda_home: float | None = None
    lambda_away: float | None = None
    fit_error: float | None = None


def american_to_decimal(odds: float) -> float:
    odds = float(odds)
    if odds == 0:
        raise ValueError("American odds cannot be zero")
    return 1.0 + (odds / 100.0 if odds > 0 else 100.0 / -odds)


def proportional_devig(odds: Iterable[float]) -> np.ndarray:
    odds = np.asarray(tuple(odds), dtype=float)
    if np.any(odds <= 1.0):
        raise ValueError("Decimal odds must be > 1")
    implied = 1.0 / odds
    return implied / implied.sum()


def source_overround(odds_1x2: Iterable[float]) -> float:
    odds = np.asarray(tuple(odds_1x2), dtype=float)
    return float((1.0 / odds).sum() - 1.0)


def poisson_matrix(lh: float, la: float, max_goals: int = 12) -> np.ndarray:
    ph = np.array([math.exp(-lh) * lh**k / math.factorial(k) for k in range(max_goals + 1)])
    pa = np.array([math.exp(-la) * la**k / math.factorial(k) for k in range(max_goals + 1)])
    return np.outer(ph, pa)


def score_outcomes(lh: float, la: float, max_goals: int = 12):
    m = poisson_matrix(lh, la, max_goals)
    home = float(np.tril(m, -1).sum())
    draw = float(np.trace(m))
    away = float(np.triu(m, 1).sum())
    return home, draw, away, m


def fit_lambdas_from_1x2(odds_1x2: Iterable[float]) -> tuple[float, float, float]:
    target = proportional_devig(odds_1x2)

    def objective(x):
        h, d, a, _ = score_outcomes(float(x[0]), float(x[1]))
        return (h - target[0])**2 + (d - target[1])**2 + (a - target[2])**2

    result = minimize(objective, np.array([1.5, 1.1]), bounds=((0.05, 5.0), (0.05, 5.0)))
    if not result.success:
        raise RuntimeError(result.message)
    return float(result.x[0]), float(result.x[1]), float(result.fun)


def market_probability(market: str, odds_1x2: Iterable[float]) -> tuple[float, float | None, float | None, float | None]:
    market = market.upper()
    p1x2 = proportional_devig(odds_1x2)

    if market == "DOUBLE_CHANCE_12":
        return float(1.0 - p1x2[1]), None, None, None
    if market == "DOUBLE_CHANCE_1X":
        return float(1.0 - p1x2[2]), None, None, None
    if market == "DOUBLE_CHANCE_X2":
        return float(1.0 - p1x2[0]), None, None, None

    lh, la, err = fit_lambdas_from_1x2(odds_1x2)
    total = lh + la

    if market == "HOME_TEAM_OVER_0.5":
        p = 1.0 - math.exp(-lh)
    elif market == "AWAY_TEAM_OVER_0.5":
        p = 1.0 - math.exp(-la)
    elif market == "HOME_TEAM_UNDER_2.5":
        p = sum(math.exp(-lh) * lh**k / math.factorial(k) for k in range(3))
    elif market == "AWAY_TEAM_UNDER_2.5":
        p = sum(math.exp(-la) * la**k / math.factorial(k) for k in range(3))
    elif market == "TOTAL_OVER_1.5":
        p = 1.0 - math.exp(-total) * (1.0 + total)
    elif market == "TOTAL_UNDER_3.5":
        p = sum(math.exp(-total) * total**k / math.factorial(k) for k in range(4))
    elif market == "TOTAL_UNDER_4.5":
        p = sum(math.exp(-total) * total**k / math.factorial(k) for k in range(5))
    else:
        raise ValueError(f"Unsupported market: {market}")
    return float(p), lh, la, err


def price_market(market: str, odds_1x2: Iterable[float]) -> ProxyPrice:
    odds_1x2 = tuple(float(x) for x in odds_1x2)
    p, lh, la, err = market_probability(market, odds_1x2)
    margin = source_overround(odds_1x2)
    fair_decimal = 1.0 / p
    # Proportional re-vig assumption. Cap only prevents an impossible sub-1.00 quote.
    offered_implied = min(0.995, p * (1.0 + margin))
    proxy_decimal = 1.0 / offered_implied
    return ProxyPrice(
        market=market,
        source_odds_1x2=odds_1x2,
        source_overround=margin,
        fair_probability=p,
        fair_decimal=fair_decimal,
        proxy_decimal=proxy_decimal,
        lambda_home=lh,
        lambda_away=la,
        fit_error=err,
    )


def parlay_decimal(*legs: ProxyPrice) -> float:
    out = 1.0
    for leg in legs:
        out *= leg.proxy_decimal
    return float(out)
