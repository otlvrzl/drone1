import pymavlink.mavutil

# connect to vehicle
vehicle = pymavlink.mavutil.mavlink_connection(device="udpin:127.0.0.1:14560")

# wait for a heartbeat
vehicle.wait_heartbeat(timeout=5)

# debugging messages
print("Connected to the vehicle")
print("Target system:", vehicle.target_system, "Target component:", vehicle.target_component)
