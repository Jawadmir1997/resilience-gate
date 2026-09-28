# ResilienceGate — Architecture

## 1. System Architecture

```mermaid
flowchart TB
    subgraph L1["Layer 1 — Operational Resilience"]
        direction TB
        SRC1["Service telemetry<br/>latency · errors · CPU · memory"]
        ING["Ingestion & normalization<br/>telemetry/ingest.py"]
        STORE[("Time-series store<br/>SQLite")]
        DET["Baseline detection<br/>EWMA + z-score<br/>detection/baseline.py"]
        SRC1 --> ING --> STORE --> DET
    end

    subgraph L2["Layer 2 — Delivery Integrity"]
        direction TB
        SRC2["Release artifact<br/>requirements · SBOM"]
        SBOM["SBOM generation<br/>CycloneDX<br/>supplychain/sbom.py"]
        OSV["Vulnerability resolution<br/>OSV database<br/>supplychain/osv.py"]
        SRC2 --> SBOM --> OSV
    end

    POL["Policy engine<br/>declarative YAML rules<br/>policy/engine.py"]
    EXP["Explanation layer<br/>explain/narrate.py"]
    OUT{"Gate decision"}

    DET -->|"scored anomalies"| POL
    OSV -->|"dependency findings"| POL
    POL --> EXP --> OUT

    OUT -->|ALLOW| SHIP["Deployment proceeds"]
    OUT -->|BLOCK| STOP["Deployment refused<br/>with stated reasons"]
```

The two layers are independent up to the policy engine and converge at a single decision point. That convergence is the design claim: neither operational state nor artifact integrity is sufficient alone.
