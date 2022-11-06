
import time
import pymavlink.mavutil as utility
import pymavlink.dialects.v20.all as dialect

# connect to vehicle
vehicle = utility.mavlink_connection(device="udpin:127.0.0.1:14560")

# wait for a heartbeat
vehicle.wait_heartbeat()

# inform user
print("Connected to system:", vehicle.target_system, ", component:", vehicle.target_component)

"""
# create set relay command
command = dialect.MAVLink_command_long_message(target_system=vehicle.target_system,
                                               target_component=vehicle.target_component,
                                               command=dialect.MAV_CMD_DO_SET_RELAY,
                                               confirmation=0,
                                               param1=1,  # relay pin instance number, starts from 0, 0 = first relay
                                               param2=1,  # 1 = ON, 0 = OFF
                                               param3=0,
                                               param4=0,
                                               param5=0,
                                               param6=0,
                                               param7=0)
# send command to the vehicle
vehicle.mav.send(command)

"""
# create repeat relay command
command = dialect.MAVLink_command_long_message(target_system=vehicle.target_system,
                                               target_component=vehicle.target_component,
                                               command=dialect.MAV_CMD_DO_REPEAT_RELAY,
                                               confirmation=0,
                                               param1=0,  # relay pin instance number, starts from 0, 0 = first relay
                                               param2=3,  # cycle count
                                               param3=10,  # cycle period
                                               param4=0,
                                               param5=0,
                                               param6=0,
                                               param7=0)
# send command to the vehicle
vehicle.mav.send(command)




