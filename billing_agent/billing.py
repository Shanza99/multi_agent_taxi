from fastapi import FastAPI

app = FastAPI()

@app.post("/calculate_fare")
def calculate_fare(ride: dict):
    distance = len(ride["pickup"] + ride["dropoff"]) * 2
    fare = distance * 10
    return {"fare": fare, "currency": "PKR"}

@app.post("/pay")
def pay(details: dict):
    return {"status": "payment successful", "amount": details["fare"], "currency": "PKR"}
