from pydantic import BaseModel
from datetime import date, datetime, time, timedelta


class Ticket_data(BaseModel):
    flight_id: int
    price: int
    data_form: datetime
    data_to: datetime
    passenger_id: int


class Passenger_data(BaseModel):
    passport: int
    first_name: str
    last_name: str

class Flight_data(BaseModel):
    space_count: int
    from_city: str
    to_city: str
    

class Order_data(BaseModel):
    ticket_id: int
    passenger_id: int
    amount : int
