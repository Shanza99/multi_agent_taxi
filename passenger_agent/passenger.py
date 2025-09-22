from fastapi import FastAPI
import requests

app = FastAPI()

@app.post("/request_ride")
def request_ride(passenger: dict):
    response = requests.post("http://localhost:8003/find_driver", json=passenger)
    return {
        "status": "ride requested",
        "passenger": passenger,
        "dispatch_response": response.json()
    }
