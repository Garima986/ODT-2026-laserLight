from machine import Pin
from servo import Servo
import time

# -----------------------
# SETUP
# -----------------------

# Servos
servo_x = Servo(Pin(4, Pin.OUT))   # left-right
servo_y = Servo(Pin(5, Pin.OUT))   # up-down

# Laser
laser = Pin(18, Pin.OUT)
laser.value(1)   # keep laser ON

# Grid size
N = 45

# -----------------------
# GRID (REPLACE THIS WITH APP DATA)
# -----------------------

grid = [[0]*N for _ in range(N)]

# Example drawing (test)
# You can remove this later
for i in range(10, 35):
    grid[i][i] = 1
    grid[i][44-i] = 1

# -----------------------
# MAIN LOOP
# -----------------------

while(1):

    for y in range(N):

        # zig-zag movement (reduces jumping)
        if y % 2 == 0:
            x_range = range(N)
        else:
            x_range = range(N-1, -1, -1)

        for x in x_range:

            if grid[y][x] == 1:

                # convert grid → servo angles
                angle_x = int((x / 44) * 180)
                angle_y = int((y / 44) * 180)

                # move servos
                servo_x.write_angle(angle_x)
                servo_y.write_angle(angle_y)

                # small delay for smooth motion
                time.sleep(0.01)