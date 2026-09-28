"""Baseline anomaly detection for ResilienceGate.

This module defines the interface for establishing a statistical baseline
from normalized telemetry and identifying meaningful deviations from it.
"""

from resilience_gate.models import Anomaly, MetricPoint


def calculate_baseline(points: list[MetricPoint]) -> dict[str, float]:
    """Calculate baseline statistics from normalized telemetry."""
    raise NotImplementedError


def detect_anomalies(
    points: list[MetricPoint],
    baseline: dict[str, float],
) -> list[Anomaly]:
    """Compare telemetry against a baseline and return detected anomalies."""
    raise NotImplementedError
