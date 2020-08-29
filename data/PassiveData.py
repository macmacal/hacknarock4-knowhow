from datetime import datetime
from dataclasses import dataclass


@dataclass
class PassiveData:
    id: int
    name: str
    producer: str = ''
    model: str = ''
    serial_number: int = 0
    activation_date: datetime = datetime.now()
    acquire_date: datetime = datetime.now()
    ports = {}
    other = {}
