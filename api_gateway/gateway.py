from fastapi import FastAPI
import requests

app = FastAPI()

@app.post("/ride")
def create_ride(passenger: dict):
    response = requests.post("http://localhost:8001/request_ride", json=passenger)
    return response.json()
