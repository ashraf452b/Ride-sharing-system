from abc import ABC, abstractmethod
from ride import RideRequest,RideMatching
class Ride_sharing:
    def __init__(self,name):
        self.name=name
        self.drivers=[]
        self.riders=[]
        self.rides=[]
    
    def add_rider(self,rider):
        self.riders.append(rider)

    def add_driver(self,driver):
        self.drivers.append(driver)
    
    def __repr__(self):
        return f'Company Name {self.name} with {len(self.drivers)} Drivers and {len(self.rides)} Rides'
    

class User(ABC):
    def __init__(self,name,email,nid):
        self.name=name
        self.email=email
        self.nid=nid
    
    @abstractmethod
    def display_profile(self):
        raise NotImplementedError
    

class Rider(User):
    def __init__(self,name,email,nid,initial_amount,current_location):
        super().__init__(name,email,nid)
        self.current_ride=None
        self.wallet=initial_amount
        self.current_location=current_location

    def display_profile(self):
        print(f'Rider Name = {self.name}\nEmail = {self.email}')
    
    def load_cash(self,amount):
        if amount>0:
            self.wallet+=amount
        else:
            print('Faild! Amount Less than zero')
    
    def request_ride(self,ride_sharing,destination,vehicle_type):
        ride_request=RideRequest(self,destination)
        ride_matching=RideMatching(ride_sharing.drivers)
        ride=ride_matching.find_driver(ride_request,vehicle_type)
        self.current_ride=ride
        print('YAY! We got a ride')

    def show_current_ride(self):
        print(self.current_ride)



class Driver(User):
    def __init__(self,name,email,nid,current_location):
        super().__init__(name,email,nid)
        self.current_location=current_location
        self.wallet=0

    def display_profile(self):
        print(f'Driver Name = {self.name}') 

    def accept_ride(self,ride):
        ride.start_ride()
        ride.set_driver(self)

    def reach_destination(self,ride):
        ride.end_ride()






    