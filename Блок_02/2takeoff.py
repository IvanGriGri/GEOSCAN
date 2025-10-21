from pioneer_sdk import *
import time

mk=Pioneer()
try:
    mk.arm()
    time.sleep(1)
    mk.takeoff()
    input()
    mk.land()
    time.sleep(2)
finally:
    mk.disarm()