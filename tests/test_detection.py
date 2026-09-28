"""Tests for ResilienceGate baseline anomaly detection."""

from datetime import datetime

from resilience_gate.detection.baseline import build_baseline, detect_anomalies
from resilience_gate.models import MetricPoint, Severity


def make_point(value: float) -> MetricPoint:
    """Create one synthetic latency metric for testing."""
    return MetricPoint(
        timestamp=datetime(2026, 9, 28, 10, 0, 0),
        service="checkout",
        metric="latency_ms",
        value=value,
        unit="ms",
    )


def test_build_baseline():
    """Baseline should calculate the expected mean."""
    points = [
        make_point(100),
        make_point(110),
        make_point(120),
    ]

    baseline_mean, baseline_std = build_baseline(points)

    assert baseline_mean == 110
    assert baseline_std > 0


def test_detect_critical_anomaly():
    """A large deviation should be detected as a critical anomaly."""
    baseline_points = [
        make_point(118),
        make_point(119),
        make_point(120),
        make_point(121),
        make_point(122),
    ]

    baseline_mean, baseline_std = build_baseline(baseline_points)

    current_points = [
        make_point(120),
        make_point(500),
    ]

    anomalies = detect_anomalies(
        current_points,
        baseline_mean,
        baseline_std,
    )

    assert len(anomalies) == 1
    assert anomalies[0].severity == Severity.CRITICAL
    assert anomalies[0].observed == 500
