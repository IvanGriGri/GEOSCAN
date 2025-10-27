from pioneer_sdk import *
import time

mk=Pioneer()
while True:
    time.sleep(3)
    for n in range(0, 4):
        mk.led_control(n, 1, 1, 1)
        time.sleep(0.5)
        mk.led_control(n, 0, 0, 0)
        time.sleep(0.5)