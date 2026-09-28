"""Local storage interface for ResilienceGate.

This module defines lightweight local persistence helpers for prototype
telemetry, findings, and deployment gate results. It is intentionally
simple and does not represent a production database layer.
"""

from resilience_gate.models import GateDecision, MetricPoint


def save_metrics(points: list[MetricPoint], path: str) -> None:
    """Save normalized telemetry points to local storage."""
    raise NotImplementedError


def save_decision(decision: GateDecision, path: str) -> None:
    """Save a deployment gate decision to local storage."""
    raise NotImplementedError
