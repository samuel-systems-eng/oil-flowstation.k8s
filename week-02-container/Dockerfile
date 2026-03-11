FROM python:3.9-slim

WORKDIR /app

# NEW: Installation of MQTT library required for Week 2
RUN pip install paho-mqtt

COPY mock_plc_v2.py .

CMD ["python", "mock_plc_v2.py"]