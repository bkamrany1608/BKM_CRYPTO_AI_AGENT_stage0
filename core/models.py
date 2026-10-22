from dataclasses import dataclass
from datetime import datetime, timezone
from enum import Enum

class Decision(str, Enum):
    TRADE = "TRADE"
    NO_TRADE = "NO_TRADE"

@dataclass(frozen=True)
class Candle:
    symbol: str
    timeframe: str
    timestamp_ms: int
    open: float
    high: float
    low: float
    close: float
    volume: float
    closed: bool = True

@dataclass(frozen=True)
class DataQuality:
    ok: bool
    reasons: tuple[str, ...] = ()

@dataclass(frozen=True)
class Signal:
    symbol: str
    timeframe: str
    direction: str
    decision: Decision
    confidence: float
    evidence: tuple[str, ...]
    quality: DataQuality
    created_at: str

@dataclass(frozen=True)
class RiskPlan:
    approved: bool
    quantity: float
    planned_loss: float
    risk_fraction: float
    reasons: tuple[str, ...] = ()
