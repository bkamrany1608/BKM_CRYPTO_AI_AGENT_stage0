# Capability matrix v0.1

| Capability | Status | Evidence |
|---|---|---|
| Local SQLite persistence | implemented | `database/store.py`, tests |
| Candle quality and freshness gate | implemented | `data/quality.py`, tests |
| Deterministic swing/VWAP/ATR primitives | implemented | `analysis/primitives.py`, tests |
| Risk sizing and 0.3R design cap | implemented | `risk/engine.py`, tests |
| Paper fill with fees/slippage | implemented | `paper_trading/engine.py`, tests |
| Live exchange adapter | pending | interface only |
| Flutter Android app/APK | pending | not implemented |
| Telegram integration | pending | not implemented |
| Probability calibration and walk-forward | pending | test contract documented |
| Excel reports | pending | schema to be finalized |
