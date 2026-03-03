from abc import ABC, abstractmethod
from Ride import rideRequest, Ride_matching
class User(ABC):
    def __init__(self, name, email,nid):
        self.name=name
        self.email=email
        self.nid=nid

    
    @abstractmethod
    def display_profile(self):
        raise NotImplementedError
    
class Rider(User):
    def __init__(self,  name, email,nid,current_location,initial_amount):
        super().__init__(name,email,nid)
        self.current_location=current_location
        self.wallet=initial_amount
        self.current_ride=None
    
    def display_profile(self):
        print(f"Rider : {self.name} and email {self.email}")

    def load_cash(self, amount):
        if amount>0:
            self.wallet+=amount
        else:
            print("Amount  Less than zero")

    def update_lcation(self,current_location):
        self.current_location=current_location

    def request_ride(self,ride_shareing,destination,vehicle_type):
         ride_request=rideRequest(self,destination)
         ride_matching=Ride_matching(ride_shareing.drivers)
         ride=ride_matching.find_driver(ride_request,vehicle_type)
         self.current_ride=ride
         print("We Got Ride!!!!!!!!!")

    def show_current_ride(self):
        print(self.current_ride)



class Driver(User):
    def __init__(self, name, email, nid, current_location):
        super().__init__(name, email,nid)
        self.current_location=current_location
        self.wallet=0

    def display_profile(self):
        print(f"Driver Name {self.name} Current Location {self.current_location}")

    def accept_ride(self,ride):
        ride.start_ride()
        ride.set_driver(self) 

    def reach_destination(self,ride):
        ride.end_ride()