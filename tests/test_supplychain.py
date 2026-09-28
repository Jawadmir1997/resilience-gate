"""Tests for ResilienceGate software supply-chain handling."""

import json

from resilience_gate.supplychain.sbom import load_cyclonedx


def test_load_cyclonedx(tmp_path):
    """CycloneDX components should be normalized into package/version pairs."""
    path = tmp_path / "sbom.json"

    path.write_text(
        json.dumps(
            {
                "bomFormat": "CycloneDX",
                "specVersion": "1.5",
                "components": [
                    {
                        "type": "library",
                        "name": "requests",
                        "version": "2.31.0",
                    },
                    {
                        "type": "library",
                        "name": "PyYAML",
                        "version": "6.0.1",
                    },
                ],
            }
        ),
        encoding="utf-8",
    )

    dependencies = load_cyclonedx(str(path))

    assert dependencies == [
        ("requests", "2.31.0"),
        ("PyYAML", "6.0.1"),
    ]


def test_load_cyclonedx_ignores_incomplete_components(tmp_path):
    """Components without a name or version should be ignored."""
    path = tmp_path / "sbom.json"

    path.write_text(
        json.dumps(
            {
                "bomFormat": "CycloneDX",
                "components": [
                    {
                        "type": "library",
                        "name": "requests",
                        "version": "2.31.0",
                    },
                    {
                        "type": "library",
                        "name": "missing-version",
                    },
                ],
            }
        ),
        encoding="utf-8",
    )

    dependencies = load_cyclonedx(str(path))

    assert dependencies == [("requests", "2.31.0")]
