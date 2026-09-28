"""Generate synthetic telemetry for ResilienceGate demos and tests.

Synthetic data keeps the prototype reproducible and avoids the use of
real employer, customer, or production data.
"""

from datetime import datetime, timedelta

from resilience_gate.models import MetricPoint


def generate_normal(
    service: str = "checkout",
    count: int = 100,
) -> list[MetricPoint]:
    """Generate a stable synthetic telemetry series."""
    raise NotImplementedError


def generate_incident(
    service: str = "checkout",
    count: int = 100,
) -> list[MetricPoint]:
    """Generate synthetic telemetry containing a simulated service incident."""
    raise NotImplementedError
