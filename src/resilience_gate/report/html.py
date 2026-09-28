"""HTML reporting interface for ResilienceGate.

This module defines how a deployment gate decision can be rendered as a
simple human-readable HTML report for review and prototype demonstrations.
"""

from resilience_gate.models import GateDecision


def render_html(decision: GateDecision) -> str:
    """Render a gate decision as an HTML document."""
    raise NotImplementedError


def save_html(decision: GateDecision, path: str) -> None:
    """Render a gate decision and save the HTML report to a file."""
    raise NotImplementedError
