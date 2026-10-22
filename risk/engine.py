from core.models import RiskPlan

def plan_risk(equity: float, entry: float, stop: float, max_risk_fraction: float = 0.003, max_quantity: float | None = None) -> RiskPlan:
    if equity <= 0 or entry <= 0 or stop <= 0 or entry == stop:
        return RiskPlan(False, 0.0, 0.0, max_risk_fraction, ("invalid_inputs",))
    distance = abs(entry-stop)
    planned_loss = equity * max_risk_fraction
    quantity = planned_loss / distance
    if max_quantity is not None and quantity > max_quantity:
        quantity = max_quantity
        planned_loss = quantity * distance
    if quantity <= 0:
        return RiskPlan(False, 0.0, 0.0, max_risk_fraction, ("zero_quantity",))
    return RiskPlan(True, quantity, planned_loss, planned_loss/equity)
