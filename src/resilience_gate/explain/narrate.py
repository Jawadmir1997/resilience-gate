"""Human-readable explanations for ResilienceGate decisions."""

from resilience_gate.models import Decision, GateDecision


def narrate(decision: GateDecision) -> str:
    """Create a concise human-readable explanation of a gate decision."""
    if decision.decision == Decision.BLOCK:
        opening = "Deployment blocked because high-risk signals were detected."
    elif decision.decision == Decision.WARN:
        opening = "Deployment allowed with warning because moderate-risk signals were detected."
    else:
        opening = "Deployment allowed because no blocking risk signals were detected."

    details = []

    if decision.anomalies:
        details.append(
            f"{len(decision.anomalies)} operational anomaly or anomalies detected."
        )

    if decision.findings:
        details.append(
            f"{len(decision.findings)} dependency vulnerability finding or findings detected."
        )

    if decision.rules_fired:
        details.append(
            "Policy rules triggered: " + ", ".join(decision.rules_fired) + "."
        )

    if not details:
        details.append("No operational anomalies or dependency vulnerabilities were detected.")

    return " ".join([opening] + details)
