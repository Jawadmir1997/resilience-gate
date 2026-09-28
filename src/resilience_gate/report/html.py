"""HTML reporting utilities for ResilienceGate."""

from html import escape

from resilience_gate.models import GateDecision


def render_html(decision: GateDecision) -> str:
    """Render a gate decision as a human-readable HTML report."""
    anomaly_rows = ""

    for anomaly in decision.anomalies:
        anomaly_rows += f"""
        <tr>
            <td>{escape(anomaly.service)}</td>
            <td>{escape(anomaly.metric)}</td>
            <td>{anomaly.observed}</td>
            <td>{anomaly.baseline}</td>
            <td>{anomaly.severity.value.upper()}</td>
            <td>{escape(anomaly.explanation)}</td>
        </tr>
        """

    finding_rows = ""

    for finding in decision.findings:
        finding_rows += f"""
        <tr>
            <td>{escape(finding.package)}</td>
            <td>{escape(finding.version)}</td>
            <td>{escape(finding.vulnerability_id)}</td>
            <td>{finding.severity.value.upper()}</td>
            <td>{escape(finding.summary)}</td>
        </tr>
        """

    rules = ", ".join(decision.rules_fired) if decision.rules_fired else "None"

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>ResilienceGate Decision Report</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 40px;
            line-height: 1.5;
        }}

        h1, h2 {{
            margin-bottom: 8px;
        }}

        .decision {{
            font-size: 28px;
            font-weight: bold;
            margin: 20px 0;
        }}

        table {{
            border-collapse: collapse;
            width: 100%;
            margin-bottom: 30px;
        }}

        th, td {{
            border: 1px solid #ccc;
            padding: 8px;
            text-align: left;
        }}

        th {{
            background: #f2f2f2;
        }}

        .meta {{
            color: #555;
        }}
    </style>
</head>
<body>
    <h1>ResilienceGate Decision Report</h1>

    <p class="meta">
        Evaluated at: {escape(decision.evaluated_at.isoformat())}
    </p>

    <div class="decision">
        Decision: {escape(decision.decision.value.upper())}
    </div>

    <h2>Explanation</h2>
    <p>{escape(decision.explanation or "No additional explanation provided.")}</p>

    <h2>Policy Rules Fired</h2>
    <p>{escape(rules)}</p>

    <h2>Operational Anomalies</h2>
    <table>
        <tr>
            <th>Service</th>
            <th>Metric</th>
            <th>Observed</th>
            <th>Baseline</th>
            <th>Severity</th>
            <th>Explanation</th>
        </tr>
        {anomaly_rows}
    </table>

    <h2>Dependency Findings</h2>
    <table>
        <tr>
            <th>Package</th>
            <th>Version</th>
            <th>Vulnerability</th>
            <th>Severity</th>
            <th>Summary</th>
        </tr>
        {finding_rows}
    </table>
</body>
</html>
"""


def save_html(decision: GateDecision, path: str) -> None:
    """Render a gate decision and save the HTML report."""
    html = render_html(decision)

    with open(path, "w", encoding="utf-8") as file:
        file.write(html)
