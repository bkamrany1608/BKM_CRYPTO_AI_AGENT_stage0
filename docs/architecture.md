# Architecture v0.1

## Non-negotiable safety rules

- Spot crypto first; futures are a separate adapter and are out of scope for this stage.
- Closed candles and forming candles are different records. Backtests may use only data available at decision time.
- Stale, incomplete, duplicated, out-of-order, or time-invalid data produces `NO_TRADE`.
- Paper mode is the default. Live mode requires explicit enablement, exchange capability checks, idempotency, reconciliation, and an emergency stop.
- R is the initial planned monetary loss at entry. Slippage, gaps, fees, and exchange failure can exceed the planned loss and must be reported.
- No claimed accuracy target is accepted without an independent labelled set, confidence intervals, and out-of-sample evidence.

## Module boundaries

- `data`: OHLCV normalization, quality checks, freshness, gap detection.
- `database`: durable SQLite schema and restart-safe state.
- `analysis`: deterministic market-structure primitives. Every output carries evidence, timestamp, timeframe, and data quality.
- `statistics`: probability definitions, calibration, bootstrap, and walk-forward evaluation.
- `risk`: position sizing, portfolio caps, daily loss guard, and safe-state decisions.
- `paper_trading`: realistic fills, fees, slippage, virtual positions, and outcome journal.
- `execution`: exchange adapter protocol only in this stage; live implementation pending.
- `app`: future Flutter control panel. No APK is claimed here.
- `reports`: reproducible metrics and XLSX export, pending after schema stabilization.

## Event flow

`source -> normalizer -> quality gate -> local store -> analysis modules -> evidence aggregator -> probability/risk gate -> paper or adapter -> reconciliation -> journal -> reports`

A failed quality gate stops downstream order decisions. Each decision must be reproducible from stored input data, parameter version, model version, and code version.

## State model

`SAFE_INIT -> PAPER_READY -> SIGNAL_CANDIDATE -> RISK_APPROVED -> PAPER_OPEN -> PAPER_MANAGED -> CLOSED`

Any stale data, uncertain order state, reconciliation mismatch, API failure, or invalid calculation transitions to `SAFE_MODE`; it cannot open a new trade until resolved.

## Explicit non-goals in v0.1

- Guaranteed win rate or profit.
- Automatic self-modification of risk rules.
- Direct live trading.
- Unverified claims of 95-100% detection accuracy.
