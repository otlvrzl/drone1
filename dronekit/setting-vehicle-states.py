
import time
import dronekit

print("Trying to connect to the vehicle...")
vehicle = dronekit.connect(ip="127.0.0.1:14550", wait_ready=True)
print("Connected to the vehicle.")

# arm the vehicle
vehicle.armed = True
print("Sent arm command.")

time.sleep(5)
print("Arm status:", vehicle.armed)

# disarm the vehicle
vehicle.armed = False
print("Sent disarm command.")

time.sleep(5)
print("Arm status:", vehicle.armed)

# change flight mode
vehicle.mode = dronekit.VehicleMode("GUIDED")
print("Sent change mode command.")

time.sleep(5)
print("Vehicle mode:", vehicle.mode.name)

print("Closing the vehicle...")
vehicle.close()
print("Closed the vehicle.")
