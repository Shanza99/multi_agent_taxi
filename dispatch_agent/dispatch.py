from fastapi import FastAPI
import requests

app = FastAPI()

@app.post("/find_driver")
def find_driver(passenger: dict):
    print("🚖 Dispatch received request:", passenger)

    # Step 1: Ask Driver Agent for a driver
    driver_response = requests.post("http://localhost:8002/assign_driver", json=passenger)
    driver_data = driver_response.json()
    print("➡️ Driver Agent replied:", driver_data)

    if driver_data.get("status") == "driver assigned":
        # Step 2: Ask Billing Agent for fare
        billing_response = requests.post("http://localhost:8004/calculate_fare", json=passenger)
        billing_data = billing_response.json()
        print("💰 Billing Agent replied:", billing_data)

        # ✅ Explicitly pull out driver and fare into final response
        return {
            "status": "ride confirmed",
            "passenger": {
                "name": passenger.get("name"),
                "pickup": passenger.get("pickup"),
                "dropoff": passenger.get("dropoff")
            },
            "driver": driver_data.get("driver"),
            "fare": {
                "fare": billing_data.get("fare"),
                "currency": billing_data.get("currency")
            }
        }
    else:
        return {"status": "no driver available"}
