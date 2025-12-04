from abc import ABC, abstractmethod
class User(ABC):
    def __init__(self,name,email,nid):
        self.name=name
        self.email=email
        self.nid=nid
    
    @abstractmethod
    def disply_profile(self):
        raise NotImplementedError
    

class Rider(User):
    def __init__(self,name,email,nid,initial_amount,current_location):
        super().__init__(name,email,nid)
        self.current_ride=None
        self.wallet=initial_amount
        self.current_location=current_location

    def disply_profile(self):
        print(f'Rider Name = {self.name}\nEmail = {self.email}')
    
    def load_cash(self,amount):
        if amount>0:
            self.wallet+=amount
        else:
            print('Faild! Amount Less than zero')
    
    def request_ride(self,ride_sharing,destination):
        pass

    def show_current_ride(self):
        print(self.current_ride)



class Driver(User):
    def __init__(self,name,email,nid,current_location):
        super().__init__(name,email,nid)
        self.current_location=current_location
        self.wallet=0

    def disply_profile(self):
        print(f'Driver Name = {self.name}') 

    def accept_ride(self,ride):
        ride.set_driver(self)
