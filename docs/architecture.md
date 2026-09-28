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

## 2. Data Flow

```mermaid
flowchart LR
    A["Raw metrics<br/>JSON / CSV"] --> B["MetricPoint<br/>normalized"]
    B --> C[("SQLite")]
    C --> D["Rolling baseline<br/>per service+metric"]
    D --> E["Anomaly<br/>score 0-1 + severity"]

    F["requirements.txt"] --> G["CycloneDX SBOM"]
    G --> H["OSV query<br/>cached"]
    H --> I["DependencyFinding<br/>CVE + severity"]

    E --> J["Policy evaluation"]
    I --> J
    J --> K["GateDecision<br/>+ rules fired"]
    K --> L["Human-readable<br/>justification"]
    L --> M["Exit code<br/>+ HTML report"]
```

## 3. Deployment Gate Sequence

```mermaid
sequenceDiagram
    participant CI as CI pipeline
    participant RG as ResilienceGate
    participant TS as Telemetry store
    participant OSV as OSV database
    participant Op as Operator

    CI->>RG: rg gate --service checkout --sbom sbom.json
    RG->>TS: fetch recent metrics for target service
    TS-->>RG: time-series window
    RG->>RG: score deviation against rolling baseline
    RG->>OSV: resolve declared dependencies
    OSV-->>RG: known vulnerabilities + severities
    RG->>RG: evaluate policy across both signal sets

    alt All rules pass
        RG-->>CI: ALLOW (exit 0)
        CI->>CI: deployment proceeds
    else Any rule blocks
        RG-->>CI: BLOCK (exit 1) + justification
        CI->>Op: surface every rule that fired, with reasons
        Op->>Op: remediate, or record an explicit policy exception
    end
```

The operator branch is deliberate. The system refuses a deployment and explains itself; it does not act unilaterally without recourse. This is the human-oversight boundary described in the XR-ACD framework.
