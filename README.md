Flowstation SRE Journal

WEEK - 01

# 🛢️ Oil Flowstation Edge Monitoring (Kubernetes)

[...Existing Architecture Overview...]

## 📈 Learning Journey & SRE Progress

### Week 1: Containerization & Local Simulation (COMPLETE)
**Goal:** Transition physical instrumentation logic into a cloud-native container.
*   **Activity:** Built a `mock_plc.py` to simulate a crude oil discharge line.
*   **SRE Win:** Resolved a DNS timeout in Minikube by investigating the network bridge (documented in `/week-01-container/TROUBLESHOOTING.md`).
*   **Proof of Life:** See telemetry stream [here](./week-01-container/telemetry-proof.png).
Full terminal session logs for Week 1 can be found here for audit and troubleshooting reference.

---
### Week 2: Internal Networking & Message Brokering (COMPLETE)
**Goal:** Implement a Service-Oriented Architecture (SOA) for telemetry ingestion.
*   **Activity:** Deployed an **Eclipse Mosquitto** MQTT Broker as a K8s Deployment/Service.
*   **SRE Win:** Configured **Service Discovery**, allowing the PLC pod to locate the "Data Junction Box" via DNS rather than static IPs.
*   **Proof of Connectivity:** Successfully verified the MQTT handshake and message publication via `kubectl logs` (see full terminals for details).

---
### Week 3: Data Persistence & The Digital Historian (COMPLETE)
**Goal:** Ensure flowstation telemetry survives pod failures using Persistent Volumes.
*   **Activity:** Deployed **InfluxDB** with a **PersistentVolumeClaim (PVC)** to act as a long-term data historian.
*   **Infrastructure:** Configured **Telegraf** as a data bridge to subscribe to MQTT topics and write time-series data to the historian.
*   **SRE Win:** Performed a "Fault Tolerance Test" by deleting the InfluxDB pod and verifying that the database automatically recovered its previous state from the persistent disk.
*   **Status:** Full Data Pipeline (PLC -> MQTT -> Telegraf -> InfluxDB) is OPERATIONAL.

### Week 4: The Digital Control Room & HMI (COMPLETE)
**Goal:** Build a professional Human-Machine Interface (HMI) to visualize flowstation health in real-time.
**Activity:** Deployed Grafana as a centralized monitoring hub, connected via a Kubernetes Service (NodePort) to a local browser.
**Observability:** Engineered a live dashboard using Flux (InfluxDB Query Language) to plot real-time pressure and flow telemetry.
**Infrastructure-as-Code:** Configured Grafana Persistence using a PersistentVolumeClaim (PVC). Verified that custom dashboards and "High Pressure" alert thresholds survive pod restarts and cluster reboots.
**SRE Win:** Implemented Visual Thresholds (60 PSI Yellow / 80 PSI Red) to simulate industrial alarm setpoints. Performed a "Chaos Test" by deleting the Grafana pod and verifying 0% data loss in the HMI configuration.
