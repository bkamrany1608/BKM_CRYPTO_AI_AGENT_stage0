import sqlite3
from core.models import Candle

SCHEMA = """CREATE TABLE IF NOT EXISTS candles(symbol TEXT, timeframe TEXT, timestamp_ms INTEGER, open REAL, high REAL, low REAL, close REAL, volume REAL, closed INTEGER, PRIMARY KEY(symbol,timeframe,timestamp_ms));"""

def connect(path: str = ":memory:"):
    db = sqlite3.connect(path)
    db.execute(SCHEMA)
    return db

def save_candles(db, candles: list[Candle]):
    db.executemany("INSERT OR REPLACE INTO candles VALUES (?,?,?,?,?,?,?,?,?)", [(c.symbol,c.timeframe,c.timestamp_ms,c.open,c.high,c.low,c.close,c.volume,int(c.closed)) for c in candles])
    db.commit()
