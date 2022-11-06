import time
import dronekit

print("Trying to connect to the vehicle...")
vehicle = dronekit.connect(ip="127.0.0.1:14550", wait_ready=True)
print("Connected to the vehicle.")

time.sleep(5)
print("Altitude: ", vehicle.location.global_relative_frame.alt)
time.sleep(5)

# request barometer calibration
vehicle.send_calibrate_barometer()
print("Requested barometer calibration")

time.sleep(5)
print("Altitude: ", vehicle.location.global_relative_frame.alt)

print("Closing the vehicle...")
vehicle.close()
print("Closed the vehicle.")
