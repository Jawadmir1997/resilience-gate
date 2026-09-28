"""Tests for ResilienceGate HTML reporting."""

from datetime import datetime

from resilience_gate.models import Decision, GateDecision
from resilience_gate.report.html import render_html, save_html


def test_render_html_contains_decision_and_sections():
    decision = GateDecision(
        decision=Decision.BLOCK,
        rules_fired=["critical_anomaly"],
        explanation="Critical anomaly detected.",
        evaluated_at=datetime(2026, 9, 28, 10, 0, 0),
    )

    html = render_html(decision)

    assert "<!DOCTYPE html>" in html
    assert "ResilienceGate Decision Report" in html
    assert "Decision: BLOCK" in html
    assert "critical_anomaly" in html
    assert "Critical anomaly detected." in html
    assert "Operational Anomalies" in html
    assert "Dependency Findings" in html


def test_save_html_writes_report(tmp_path):
    decision = GateDecision(
        decision=Decision.ALLOW,
        explanation="No significant risk detected.",
    )

    output = tmp_path / "report.html"

    save_html(decision, str(output))

    assert output.exists()
    content = output.read_text(encoding="utf-8")
    assert "Decision: ALLOW" in content
    assert "ResilienceGate Decision Report" in content
