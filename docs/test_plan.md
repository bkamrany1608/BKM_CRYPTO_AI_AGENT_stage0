# Test plan v0.1

## Test layers

1. Unit: candle validation, swing confirmation timing, VWAP/ATR, R and sizing, fee/slippage arithmetic.
2. Property: no future candle can alter a historical decision; duplicate and reordered input is rejected or normalized deterministically.
3. Integration: feed -> quality gate -> SQLite -> analysis -> risk -> paper fill -> journal.
4. Replay: bullish, bearish, range, high-volatility, gap, stale feed, partial candle, and API failure fixtures.
5. Statistical: train/validation/test separation, walk-forward windows, bootstrap intervals, calibration error, and minimum sample checks.
6. Recovery: process restart, incomplete write, unknown order state, duplicate client order id, and reconciliation mismatch.

## Release gates

- All unit and integration tests pass.
- No look-ahead test failure.
- No live adapter enabled by default.
- Risk limits are tested with boundary and adverse-slippage cases.
- Paper results include fees and slippage assumptions.
- Any probability below its minimum sample/calibration gate yields `NO_TRADE`.
- Every incomplete feature appears in the release capability matrix.

## Required future evidence

- Labelled chart set with agreed definitions and provenance.
- Independent out-of-sample period.
- Per-symbol, timeframe, regime, strategy, and session metrics.
- Confidence intervals, sample sizes, dependency handling for correlated signals.
- Demo/testnet soak period before any live permission.
