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
    start_time = datetime.now()
    points = []

    for index in range(count):
        points.append(
            MetricPoint(
                timestamp=start_time + timedelta(minutes=index),
                service=service,
                metric="latency_ms",
                value=120.0 + (index % 5),
                unit="ms",
            )
        )

    return points


def generate_incident(
    service: str = "checkout",
    count: int = 100,
) -> list[MetricPoint]:
    """Generate synthetic telemetry containing a simulated service incident."""
    points = generate_normal(service=service, count=count)

    incident_start = int(count * 0.8)

    for index in range(incident_start, count):
        points[index].value += 300.0

    return points
