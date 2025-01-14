from fastapi import FastAPI,HTTPException
from schemas import *
from models import *

app = FastAPI()

@app.post("/flight")
def flight_add(data:Flight_data):
    db = session()
    new_flight = Flight(space_count=data.space_count,from_city=data.from_city,to_city=data.to_city)
    db.add(new_flight)
    db.commit()
    db.refresh(new_flight)
    db.close()
    return new_flight