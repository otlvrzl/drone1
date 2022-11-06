
import time
import pymavlink.mavutil as utility
import pymavlink.dialects.v20.all as dialect

# connect to vehicle
vehicle = utility.mavlink_connection(device="udpin:127.0.0.1:14560")

# wait for a heartbeat
vehicle.wait_heartbeat()

# inform user
print("Connected to system:", vehicle.target_system, ", component:", vehicle.target_component)

# infinite loop
while True:

    # try to receive a message
    try:

        # receive a message
        message = vehicle.recv_match(type=dialect.MAVLink_system_time_message.msgname, blocking=True)

        # convert received message to dictionary
        message = message.to_dict()

        # for each field name in field names of this message
        for field_name in dialect.MAVLink_system_time_message.fieldnames:

            # if the field is system boot time in milliseconds
            if field_name == "time_boot_ms":

                # print field name and contained field value
                print(field_name, message[field_name])

    # bare except to catch all the exceptions
    except:

        # print that no message is received matches the condition
        print("no message received from vehicle")

    # tiny sleep to cool down the terminal
    time.sleep(0.050)
