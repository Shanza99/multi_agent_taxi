# Multi-Agent Taxi Ride Sharing Service

## Run Instructions
1. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
2. Start agents in separate terminals:
   ```bash
   uvicorn passenger_agent.passenger:app --port 8001
   uvicorn driver_agent.driver:app --port 8002
   uvicorn dispatch_agent.dispatch:app --port 8003
   uvicorn billing_agent.billing:app --port 8004
   uvicorn api_gateway.gateway:app --port 8000
   ```
3. Test with curl:
   ```bash
   curl -X POST http://localhost:8000/ride -H "Content-Type: application/json" -d '{"name":"Ali","pickup":"Mall Road","dropoff":"Airport"}'
   ```

4. Run tests:
   ```bash
   pytest tests/
   ```
