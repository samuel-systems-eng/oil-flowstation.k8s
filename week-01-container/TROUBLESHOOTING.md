# Week 1 Troubleshooting: DNS Resolution Error

### Issue
The command `minikube image build` failed with an `i/o timeout` while trying to pull the `python:3.9-slim` base image from Docker Hub.

### Diagnosis
Internal `minikube ssh "ping 8.8.8.8"` was successful, confirming internet connectivity. The failure was isolated to DNS resolution (translating `registry-1.docker.io` to an IP).

### Resolution
Restarted the local cluster using the `--dns-proxy=true` flag. This allows the Minikube VM to use the host machine's (Windows) DNS settings directly.

### SRE takeaway
In remote flowstations, satellite or cellular backhaul often has DNS instability. Using a reliable DNS proxy or local image registry is a critical reliability pattern.

![Flowstation Telemetry Stream](./week-01-container/telemetry-proof.png)
