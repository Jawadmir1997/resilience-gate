"""Policy engine for ResilienceGate deployment decisions."""

from resilience_gate.models import (
    Anomaly,
    Decision,
    DependencyFinding,
    GateDecision,
    Severity,
)


def evaluate(
    anomalies: list[Anomaly],
    findings: list[DependencyFinding],
) -> GateDecision:
    """Evaluate operational and supply-chain signals for deployment safety."""
    rules_fired = []

    critical_anomaly = any(
        anomaly.severity == Severity.CRITICAL for anomaly in anomalies
    )

    high_risk_dependency = any(
        finding.severity in (Severity.HIGH, Severity.CRITICAL)
        for finding in findings
    )

    medium_risk = any(
        anomaly.severity == Severity.MEDIUM for anomaly in anomalies
    ) or any(
        finding.severity == Severity.MEDIUM for finding in findings
    )

    if critical_anomaly:
        rules_fired.append("critical_operational_anomaly")

    if high_risk_dependency:
        rules_fired.append("high_risk_dependency")

    if critical_anomaly or high_risk_dependency:
        decision = Decision.BLOCK
    elif medium_risk:
        rules_fired.append("medium_risk_signal")
        decision = Decision.WARN
    else:
        decision = Decision.ALLOW

    return GateDecision(
        decision=decision,
        rules_fired=rules_fired,
        anomalies=anomalies,
        findings=findings,
    )
