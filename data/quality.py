from datetime import datetime, timezone
from core.models import Candle, DataQuality

def validate_candles(candles: list[Candle], now_ms: int, max_age_ms: int = 120_000) -> DataQuality:
    if not candles:
        return DataQuality(False, ("empty_feed",))
    reasons: list[str] = []
    seen = set()
    previous = None
    for c in candles:
        if not c.closed:
            reasons.append("forming_candle")
        if c.timestamp_ms in seen:
            reasons.append("duplicate_timestamp")
        seen.add(c.timestamp_ms)
        if previous is not None and c.timestamp_ms <= previous:
            reasons.append("out_of_order")
        previous = c.timestamp_ms
        if min(c.open, c.high, c.low, c.close, c.volume) < 0 or c.high < max(c.open, c.close) or c.low > min(c.open, c.close):
            reasons.append("invalid_ohlcv")
    if now_ms - candles[-1].timestamp_ms > max_age_ms:
        reasons.append("stale_feed")
    return DataQuality(not reasons, tuple(dict.fromkeys(reasons)))
