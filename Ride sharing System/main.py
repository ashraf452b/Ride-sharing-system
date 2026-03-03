from Ride import RideShareing
from User import Rider, Driver

# Create Ride Sharing Company
urao = RideShareing("Uraiya Neo")

# Create Rider
kejabe = Rider("Ami Jabo","amijabo@mail.com",12345,"Le Meridian",1500)

# Create Driver
rohomot = Driver("Rohomot","rohomot@mail.com",123455,"Airport")

# Add to system
urao.add_rider(kejabe)
urao.add_driver(rohomot)

# Initial Wallet Status
print("Before Ride:")
print("Rider Wallet:", kejabe.wallet)
print("Driver Wallet:", rohomot.wallet)
print("-" * 40)

# Request Ride
kejabe.request_ride(urao, "Uttara", "car")

# Show Ride Info
print("\nCurrent Ride Info:")
kejabe.show_current_ride()

print("-" * 40)

# Complete Ride
rohomot.reach_destination(kejabe.current_ride)

# After Ride Wallet Status
print("\nAfter Ride:")
print("Rider Wallet:", kejabe.wallet)
print("Driver Wallet:", rohomot.wallet)

print("-" * 40)

# Company Summary
print("\nSystem Summary:")
print(urao)