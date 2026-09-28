"""Policy evaluation interface for ResilienceGate.

This module defines how operational anomalies and software supply-chain
findings are evaluated to produce an explainable deployment gate decision.
"""

from resilience_gate.models import (
    Anomaly,
    DependencyFinding,
    GateDecision,
)


def evaluate_policy(
    anomalies: list[Anomaly],
    findings: list[DependencyFinding],
    policy: dict,
) -> GateDecision:
    """Evaluate current signals against policy and return a gate decision."""
    raise NotImplementedError
