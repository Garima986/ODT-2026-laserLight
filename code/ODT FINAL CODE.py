from simple_ble import BLEConnection
from machine import Pin, PWM
import time

servo_x = PWM(Pin(18), freq=50)
servo_y = PWM(Pin(19), freq=50)

CENTER_ANGLE = 160
HALF_RANGE   = 30    # ← increased from 15 to 45 for smoother curves
GRID_MAX     = 200
INVERT_Y     = False
INVERT_X     = True

def angle_to_duty_u16(angle):
    angle = max(0, min(180, angle))
    pulse_us = 500 + (angle / 180) * 2000
    return int((pulse_us / 20000) * 65535)

def grid_to_angle(x, y):
    min_a = CENTER_ANGLE - HALF_RANGE
    max_a = CENTER_ANGLE + HALF_RANGE
    ax = min_a + (x / GRID_MAX) * (max_a - min_a)
    ay = min_a + (y / GRID_MAX) * (max_a - min_a)
    if INVERT_X: ax = max_a + min_a - ax
    if INVERT_Y: ay = max_a + min_a - ay
    return int(ax), int(ay)

def move_to_point(x, y):
    ax, ay = grid_to_angle(x, y)
    servo_x.duty_u16(angle_to_duty_u16(ax))
    servo_y.duty_u16(angle_to_duty_u16(ay))

def go_home():
    servo_x.duty_u16(angle_to_duty_u16(CENTER_ANGLE))
    servo_y.duty_u16(angle_to_duty_u16(CENTER_ANGLE))
    print("Homed to", CENTER_ANGLE)

go_home()
time.sleep(0.5)

print("Starting Bluetooth...")
my_bluetooth = BLEConnection("Laser")
print(f"Ready! Range={CENTER_ANGLE}°±{HALF_RANGE}°, 16-bit PWM")

was_connected = False
flush_counter = 0

while True:
    connected = my_bluetooth.is_connected()
    if connected and not was_connected:
        print("Connected — flushing...")
        flush_counter = 5
        was_connected = True
    if not connected:
        was_connected = False

    if connected:
        if my_bluetooth.any():
            raw_data = my_bluetooth.read()
            if flush_counter > 0:
                flush_counter -= 1
                time.sleep(0.01)
                continue
            if isinstance(raw_data, bytes):
                raw_data = raw_data.decode('utf-8', errors='ignore')
            messages = raw_data.split('\n')
            last_valid = None
            is_home = False
            for msg in messages:
                clean_msg = msg.replace('\x00', '').strip()
                if not clean_msg:
                    continue
                if clean_msg.upper() == 'HOME':
                    is_home = True
                    last_valid = None
                elif ',' in clean_msg:
                    try:
                        parts = clean_msg.split(',')
                        if len(parts) != 2:
                            continue
                        x = int(float(parts[0]))
                        y = int(float(parts[1]))
                        if 0 <= x <= GRID_MAX and 0 <= y <= GRID_MAX:
                            last_valid = (x, y)
                            is_home = False
                        else:
                            print("Out of range:", x, y)
                    except Exception as e:
                        print("Invalid:", repr(clean_msg), "→", e)
            if is_home:
                go_home()
            elif last_valid:
                move_to_point(last_valid[0], last_valid[1])
                time.sleep(0.05)

    time.sleep(0.01)