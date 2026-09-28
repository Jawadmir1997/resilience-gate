"""SBOM handling interface for ResilienceGate.

This module defines how software dependency information can be extracted
from a CycloneDX Software Bill of Materials and normalized for downstream
supply-chain vulnerability analysis.
"""


def load_sbom(path: str) -> list[tuple[str, str]]:
    """Load package names and versions from a CycloneDX SBOM file."""
    raise NotImplementedError


def normalize_components(components: list[dict]) -> list[tuple[str, str]]:
    """Normalize SBOM components into package and version pairs."""
    raise NotImplementedError
