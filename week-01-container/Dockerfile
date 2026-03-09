# Use a small Python base image
FROM python:3.9-slim

# Set working directory inside the container
WORKDIR /app

# Copy mock_plc script from PC to the container
COPY mock_plc.py .

# Tell container to run script when it starts
CMD ["python", "mock_plc.py"]
