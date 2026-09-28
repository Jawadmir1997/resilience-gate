"""OSV vulnerability lookup for ResilienceGate dependencies."""

import requests

from resilience_gate.models import DependencyFinding, Severity

OSV_QUERY_URL = "https://api.osv.dev/v1/query"


def query_osv(package: str, version: str) -> list[DependencyFinding]:
    """Query OSV for known vulnerabilities affecting a Python package."""
    payload = {
        "package": {
            "name": package,
            "ecosystem": "PyPI",
        },
        "version": version,
    }

    response = requests.post(OSV_QUERY_URL, json=payload, timeout=10)
    response.raise_for_status()

    data = response.json()
    findings = []

    for vulnerability in data.get("vulns", []):
        findings.append(
            DependencyFinding(
                package=package,
                version=version,
                vulnerability_id=vulnerability.get("id", "UNKNOWN"),
                severity=Severity.MEDIUM,
                summary=vulnerability.get(
                    "summary",
                    "Known vulnerability reported by OSV.",
                ),
                explanation=(
                    f"OSV reported {vulnerability.get('id', 'UNKNOWN')} "
                    f"for {package} {version}."
                ),
            )
        )

    return findings
