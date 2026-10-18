# LENNON V2 - Forward metrics policy, 2026-10-18

Paper bankroll: MXN 1,000,000 initial; zero positions and zero new tickets. No real wager without ticket-specific written authorization. No synthetic fills without contemporaneous price.

Prediction: unique fixture Brier 1X2 (3-class sum squared errors), log loss, Over2.5 and BTTS Brier, calibration bins and counts, goal MAE/RMSE, by league/market/provenance/odds band. Compare against pre-frozen no-vig market and V0.1, paired by fixture. Track confidence intervals and n.

Financial: equity, realized/unrealized P&L, verified ROI on settled stakes, bankroll return, drawdown, turnover, open exposure, CLV only with time-stamped entry and closing prices. Historical unverified prices are not validated ROI.

Data: eligible fixture coverage, timestamp quality, duplicate/retrofreeze count, settlement completeness and CP/GitHub readback rate. No retuning from a single session. Candidate V0.2 must beat V0.1 on at least 200 paired out-of-sample fixtures and calibration, with uncertainty quantified.

Shadow edge requires validated price, >=5 percentage points over no-vig, positive after-cost EV, and independent prospective gate. Real 0 without separate user authorization. Paper risk cap 0.25% equity per ticket, 2% total exposure, 1% daily loss, 5% drawdown. These limits do not authorize execution.
