"""SBOM parsing utilities for ResilienceGate."""

import json


def load_cyclonedx(path: str) -> list[tuple[str, str]]:
    """Load package names and versions from a CycloneDX JSON SBOM."""
    with open(path, "r", encoding="utf-8") as file:
        sbom = json.load(file)

    dependencies = []

    for component in sbom.get("components", []):
        name = component.get("name")
        version = component.get("version")

        if name and version:
            dependencies.append((str(name), str(version)))

    return dependencies
