import requests

def test_ride_flow():
    passenger = {"name": "Ali", "pickup": "Mall Road", "dropoff": "Airport"}
    response = requests.post("http://localhost:8000/ride", json=passenger)
    data = response.json()
    
    assert response.status_code == 200
    assert "ride requested" in data["status"]
    assert "driver" in data["dispatch_response"]
    assert "fare" in data["dispatch_response"]
