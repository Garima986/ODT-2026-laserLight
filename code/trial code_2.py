

from machine import Pin
from servo import Servo
import time
from simple_ble import BLEConnection


# LED (startup indicator)


led = Pin(2, Pin.OUT)

led.on()
time.sleep(1)
led.off()


# SERVOS SETUP


servo_x = Servo(Pin(4, Pin.OUT))   # X axis(left right)
servo_y = Servo(Pin(5, Pin.OUT))   # Y axis(up down)

# -----------------------
# LASER
# -----------------------

laser = Pin(18, Pin.OUT)
laser.value(1)   # always ON


# BLUETOOTH CONNECTION


print("Starting Bluetooth...")
my_bluetooth = BLEConnection("Laserproject")
print("Send (x,y) in 45x45 grid")





while True:

    if my_bluetooth.is_connected():

        data = my_bluetooth.get_array()

        # Expecting [x, y]
        if data is not None and len(data) == 2:

            x = data[0]   # 0 → 44
            y = data[1]   # 0 → 44

            print("Received:", x, y)

            # convert grid → servo angle
            angle_x = int((x / 44) * 180)
            angle_y = int((y / 44) * 180)

            # move servos
            servo_x.write_angle(angle_x)
            servo_y.write_angle(angle_y)

            time.sleep(0.01)