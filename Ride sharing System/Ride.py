from datetime import datetime
from Vehicle import Car, Bike
class Ride():
    def __init__(self,start_location,end_location,vehicle):
        self.start_location=start_location
        self.end_location=end_location
        self.driver=None
        self.rider=None
        self.start_time=None
        self.estmiated_fare=None
        self.vehicle=vehicle
    
    def set_driver(self,driver):
        self.driver=driver

    def start_ride(self):
        self.start_time=datetime.now()

    def end_ride(self):
        self.end_time=datetime.now()
        self.rider.wallet-=self.estmiated_fare
        self.driver.wallet+=self.estmiated_fare
    def calculate_fare(self,distance):
        fare_per_km={
            'car':100,
            'bike' : 40,
            'cng' : 50
        }
        return distance * fare_per_km[self.vehicle.vehicle_type] 

    def __repr__(self):
        return f"Ride Details : started {self.start_location} to {self.end_location}"
    

class rideRequest:
    def __init__(self,rider,end_location):
        self.rider=rider
        self.end_location=end_location 

class Ride_matching():
    def __init__(self,drivers):
        self.avaiable_drivers=drivers

    def find_driver(self,ride_request,vehicle_type):
        if len(self.avaiable_drivers)>0:
            print('Looking for Drivers.....')
            driver=self.avaiable_drivers[0]
            
            if vehicle_type=='car':
                vechile=Car('car',"123ABC",50)
            elif vehicle_type=='bike':
                vechile=Bike('HONDA','777AAA',30)
            ride = Ride(ride_request.rider.current_location, ride_request.end_location, vechile)
            ride.rider=ride_request.rider
            ride.estmiated_fare=ride.calculate_fare(10)
            driver.accept_ride(ride) 
            return ride


class RideShareing: 
    def __init__(self,company_name):
        self.company_name=company_name
        self.riders=[]
        self.drivers=[]
        self.rides=[]
    
    def add_rider(self,rider):
        self.riders.append(rider)

    def add_driver(self,driver):
        self.drivers.append(driver)

    
    def __repr__(self):
        return f" Company Name  {self.company_name} with Rider {len(self.riders)} and Drivers {len(self.drivers)}"