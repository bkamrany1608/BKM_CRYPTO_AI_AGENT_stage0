from dataclasses import dataclass

@dataclass(frozen=True)
class Fill:
    quantity: float
    entry: float
    exit: float
    gross_pnl: float
    fees: float
    slippage: float
    net_pnl: float

def close_long(quantity: float, entry: float, exit: float, fee_rate: float = 0.001, slippage_rate: float = 0.0005) -> Fill:
    executed_entry = entry * (1 + slippage_rate)
    executed_exit = exit * (1 - slippage_rate)
    gross = quantity * (executed_exit - executed_entry)
    fees = quantity * (executed_entry + executed_exit) * fee_rate
    slippage = quantity * (entry*slippage_rate + exit*slippage_rate)
    return Fill(quantity, entry, exit, gross, fees, slippage, gross-fees)
