from pioneer_sdk import *
import time

mk=Pioneer()
while True:
    mk.led_control(255, 1, 1, 1)
    time.sleep(0.3)
    mk.led_control(255, 0, 0, 0)
    time.sleep(0.7)