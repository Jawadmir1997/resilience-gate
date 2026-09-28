"""Baseline anomaly detection for ResilienceGate telemetry."""

from statistics import mean, pstdev

from resilience_gate.models import Anomaly, MetricPoint, Severity


def build_baseline(points: list[MetricPoint]) -> tuple[float, float]:
    """Calculate the mean and standard deviation of telemetry values."""
    if not points:
        raise ValueError("Cannot build a baseline from empty telemetry.")

    values = [point.value for point in points]
    baseline_mean = mean(values)
    baseline_std = pstdev(values)

    return baseline_mean, baseline_std


def detect_anomalies(
    points: list[MetricPoint],
    baseline_mean: float,
    baseline_std: float,
) -> list[Anomaly]:
    """Detect telemetry points that significantly deviate from the baseline."""
    anomalies = []

    if baseline_std == 0:
        return anomalies

    for point in points:
        deviation_sigma = abs(point.value - baseline_mean) / baseline_std

        if deviation_sigma >= 4.0:
            severity = Severity.CRITICAL
        elif deviation_sigma >= 3.0:
            severity = Severity.HIGH
        elif deviation_sigma >= 2.0:
            severity = Severity.MEDIUM
        else:
            continue

        anomalies.append(
            Anomaly(
                timestamp=point.timestamp,
                service=point.service,
                metric=point.metric,
                observed=point.value,
                baseline=baseline_mean,
                deviation_sigma=deviation_sigma,
                score=deviation_sigma,
                severity=severity,
                explanation=(
                    f"{point.metric} for {point.service} deviated "
                    f"{deviation_sigma:.2f} standard deviations from baseline."
                ),
            )
        )

    return anomalies
