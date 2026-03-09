import time
import random
import json
def generate_flow_data():
    # Simulate a crude oil flow line
    # Normal pressure: 40-60 PSI | Normal flow: 200-250 BPH
    pressure = round(random.uniform(40, 60), 2)
    flow_rate = round(random.uniform(200, 250), 2)
    temp = round(random.uniform(70, 95), 2)
    
    # Simulate an occasional high-pressure anomaly (>5% chance)
    if random.random() > 0.95:
        pressure += 30
        
    data = {
        "timestamp": time.time(),
        "tag_id": "FS_001_MAIN_DISCHARGE",
        "pressure_psi": pressure,
        "flow_bph": flow_rate,
        "temp_f": temp,
        "status": "OPERATIONAL" if pressure < 80 else "CRITICAL_HIGH_PRESSURE"
    }
    return data
if __name__ == "__main__":
    print("--- Flowstation Mock PLC Started ---")
    while True:
        telemetry = generate_flow_data()
        print(json.dumps(telemetry))
        time.sleep(5) # Emits data every 5 seconds
