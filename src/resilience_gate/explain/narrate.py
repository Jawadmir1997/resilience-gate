"""Explainability interface for ResilienceGate.

This module converts deployment gate results into concise, human-readable
explanations so that operators can understand the signals and policy rules
behind a decision.
"""

from resilience_gate.models import GateDecision


def narrate_decision(decision: GateDecision) -> str:
    """Return a human-readable explanation of a gate decision."""
    raise NotImplementedError
