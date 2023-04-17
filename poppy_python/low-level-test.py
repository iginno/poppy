from pypot.dynamixel.io import DxlIO

with DxlIO('/dev/ttyUSB0') as dxl_io:
    motor_IDs = dxl_io.scan()
    num_motors = len(motor_IDs)
    while(True):
        print("Found", num_motors, "motors with current angles",  dxl_io.get_present_position(motor_IDs))
