from abc import ABC , abstractmethod
class Vehicle(ABC):
    speed={
        'car'   : 60,
        'bike'  : 60,
        'cng'   :15,
    }
    def __init__(self,vehicle_type,license_plate,rate):
        self.vehicle_type=vehicle_type
        self.license_plate=license_plate
        self.rate=rate

class Car(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate):
        super().__init__(vehicle_type, license_plate, rate)

class Bike(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate):
        super().__init__(vehicle_type, license_plate, rate)

class Cng(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate):
        super().__init__(vehicle_type, license_plate, rate)
