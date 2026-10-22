# Next implementation gate

Before adding live connectivity, resolve the product decisions already identified in the v1.1 specification: account-currency and capital-baseline rules, supported spot venues and symbol universe, paper-trade exit semantics, probability thresholds and sample gates, timezone boundaries, and the exact Excel scope.

The next code increment should add a provider-neutral OHLCV adapter, gap detection by timeframe, a richer SQLite journal, and replay fixtures. It must remain paper-only until those tests pass.
