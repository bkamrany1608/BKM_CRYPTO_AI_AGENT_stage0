import unittest
from core.models import Candle
from data.quality import validate_candles
from analysis.primitives import atr, vwap, confirmed_swings
from risk.engine import plan_risk
from paper_trading.engine import close_long
from database.store import connect, save_candles

class CoreTests(unittest.TestCase):
    def setUp(self):
        self.cs = [Candle("BTC/USDT","1m",i*60000, 100+i, 102+i, 99+i, 101+i, 10) for i in range(8)]

    def test_quality_rejects_stale_and_forming(self):
        bad = self.cs[:-1] + [Candle("BTC/USDT","1m",420000,107,108,106,107,10,False)]
        q = validate_candles(bad, now_ms=900000)
        self.assertFalse(q.ok)
        self.assertIn("forming_candle", q.reasons)

    def test_no_lookahead_is_explicit(self):
        swings = confirmed_swings(self.cs, 1, 1)
        for _, event_ts, confirmed_ts, _ in swings:
            self.assertGreater(confirmed_ts, event_ts)

    def test_indicators(self):
        self.assertGreater(atr(self.cs), 0)
        self.assertGreater(vwap(self.cs), 0)

    def test_risk_cap(self):
        plan = plan_risk(1000, 100, 95)
        self.assertTrue(plan.approved)
        self.assertAlmostEqual(plan.planned_loss, 3.0)

    def test_realistic_paper_fill(self):
        fill = close_long(1, 100, 110)
        self.assertLess(fill.net_pnl, 10)
        self.assertGreater(fill.fees, 0)

    def test_restart_safe_storage(self):
        db = connect()
        save_candles(db, self.cs)
        self.assertEqual(db.execute("select count(*) from candles").fetchone()[0], 8)
        save_candles(db, self.cs)
        self.assertEqual(db.execute("select count(*) from candles").fetchone()[0], 8)

if __name__ == "__main__":
    unittest.main()
