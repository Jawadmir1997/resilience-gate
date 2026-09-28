"""Tests for the ResilienceGate deployment policy engine."""

from datetime import datetime

from resilience_gate.models import (
    Anomaly,
    Decision,
    Severity,
)
from resilience_gate.policy.engine import evaluate


def make_anomaly(severity: Severity) -> Anomaly:
    """Create a synthetic anomaly for policy testing."""
    return Anomaly(
        timestamp=datetime(2026, 9, 28, 10, 0, 0),
        service="checkout",
        metric="latency_ms",
        observed=500.0,
        baseline=120.0,
        deviation_sigma=5.0,
        score=5.0,
        severity=severity,
        explanation="Synthetic anomaly for automated testing.",
    )


def test_critical_anomaly_blocks_deployment():
    """A critical operational anomaly should block deployment."""
    decision = evaluate(
        anomalies=[make_anomaly(Severity.CRITICAL)],
        findings=[],
    )

    assert decision.decision == Decision.BLOCK
    assert "critical_operational_anomaly" in decision.rules_fired


def test_medium_anomaly_warns():
    """A medium operational anomaly should produce a warning."""
    decision = evaluate(
        anomalies=[make_anomaly(Severity.MEDIUM)],
        findings=[],
    )

    assert decision.decision == Decision.WARN
    assert "medium_risk_signal" in decision.rules_fired


def test_no_risk_allows_deployment():
    """No detected risk should allow deployment."""
    decision = evaluate(
        anomalies=[],
        findings=[],
    )

    assert decision.decision == Decision.ALLOW
    assert decision.rules_fired == []
