from fastapi import FastAPI
import random

app = FastAPI()

drivers = [
    {"id": 1, "name": "Driver A", "location": "Downtown", "available": True},
    {"id": 2, "name": "Driver B", "location": "Airport", "available": True},
    {"id": 3, "name": "Driver C", "location": "University", "available": True}
]

@app.get("/drivers")
def list_drivers():
    return drivers

@app.post("/assign_driver")
def assign_driver(request: dict):
    available = [d for d in drivers if d["available"]]
    if not available:
        return {"status": "no drivers available"}
    
    chosen = random.choice(available)
    chosen["available"] = False
    return {"status": "driver assigned", "driver": chosen}
