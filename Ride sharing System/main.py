from ride import Ride,RideRequest,RideMatching
from users import Rider,Driver,Ride_sharing
from vehicle import Car,Bike,Cng

com=Ride_sharing('niye_jao')
nola=Driver('Ashraful','my@mail',123,'Airport')
com.add_driver(nola)
cus=Rider('Sherlock','your@mail',321,1000,'airport')
com.add_rider(cus)
car= Car('car','ABC123',50)
bike=Bike('bike','B876HH',45)
cng=Cng('Cng','CN654GG',35)
cus.request_ride(com,10,car)
nola.reach_destination(cus.current_ride)
cus.show_current_ride()

print(com) 