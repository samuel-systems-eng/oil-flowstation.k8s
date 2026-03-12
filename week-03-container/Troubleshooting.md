Week 3 Troubleshooting: Persistent Storage vs. Configuration Updates

The Issue
After deploying the Telegraf Bridge, logs showed a persistent 401 Unauthorized error when attempting to write telemetry data to InfluxDB, despite the MQTT_CONSUMER being successfully connected.

The Diagnosis (SRE Root Cause Analysis)
Initial Conflict: The Telegraf configuration was using a static token (my-super-secret-token), but the InfluxDB instance had already initialized with a different, auto-generated credential during the first boot.

The Persistence Trap: 
Because we successfully implemented a Persistent Volume Claim (PVC), simply restarting the InfluxDB pod or updating its environment variables did not work. InfluxDB saw the existing data on the "digital hard drive" and skipped the initialization phase where it would have accepted the new token.

The Resolution
To synchronize the security credentials across the pipeline:
Purged the State: Deleted the InfluxDB Deployment and the PersistentVolumeClaim to "wipe the drive."
Re-provisioned: Re-applied the PVC and Deployment simultaneously with the correct DOCKER_INFLUXDB_INIT_ADMIN_TOKEN.
Verified Handshake: Confirmed via kubectl logs -l app=telegraf that the 401 error was resolved and the "Digital Historian" was accepting data batches.