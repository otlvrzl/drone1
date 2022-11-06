
import time
import dronekit


def mode_callback(self, attribute_name, message):
    print(self.mode.name)


def parameter_callback(self, parameter_name, message):
    print(parameter_name, message)


def message_callback(self, message_name, message):
    print("Heartbeat:", self.last_heartbeat)


print("Trying to connect to the vehicle...")
vehicle = dronekit.connect(ip="127.0.0.1:14550", wait_ready=True)
print("Connected to the vehicle.")

#vehicle.add_attribute_listener("mode", mode_callback)
#vehicle.parameters.add_attribute_listener("SYSID_THISMAV", parameter_callback)
vehicle.add_message_listener("HEARTBEAT", message_callback)

print("observer added")

# dummy loop waiting for keyboard interrupt
try:
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    #vehicle.remove_attribute_listener("mode", mode_callback)
    #vehicle.parameters.remove_attribute_listener("SYSID_THISMAV", parameter_callback)
    vehicle.remove_message_listener("HEARTBEAT", message_callback)
    print("Closing the vehicle...")
    vehicle.close()
    print("Closed the vehicle.")


