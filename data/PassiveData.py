from datetime import datetime


class PassiveData:
    def __init__(self, id, name, producer='', model='', serial_number='', activation_date=datetime.now(),
                 acquire_date=datetime.now()):
        self.id = id
        self.name = name
        self.producer = producer
        self.model = model
        self.serial_number = serial_number
        self.activation_date = activation_date
        self.acquire_date = acquire_date
        self.ports = {}
        self.other = {}

