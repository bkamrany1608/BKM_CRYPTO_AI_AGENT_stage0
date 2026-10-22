from statistics import mean
from core.models import Candle

def atr(candles: list[Candle], period: int = 14) -> float:
    if len(candles) < 2:
        return 0.0
    trs = []
    for prev, cur in zip(candles, candles[1:]):
        trs.append(max(cur.high-cur.low, abs(cur.high-prev.close), abs(cur.low-prev.close)))
    return mean(trs[-period:]) if trs else 0.0

def vwap(candles: list[Candle]) -> float:
    total_volume = sum(c.volume for c in candles)
    return sum(((c.high+c.low+c.close)/3)*c.volume for c in candles) / total_volume if total_volume else 0.0

def confirmed_swings(candles: list[Candle], left: int = 2, right: int = 2):
    """Returns only swings whose confirmation candle has closed; no look-ahead timestamp is hidden."""
    out = []
    for i in range(left, len(candles)-right):
        window = candles[i-left:i+right+1]
        c = candles[i]
        if c.high == max(x.high for x in window):
            out.append(("high", c.timestamp_ms, candles[i+right].timestamp_ms, c.high))
        if c.low == min(x.low for x in window):
            out.append(("low", c.timestamp_ms, candles[i+right].timestamp_ms, c.low))
    return out
