from pioneer_sdk import *
import time
import math

mk=Pioneer()
mk.arm()
time.sleep(1)
mk.takeoff()
try:
    mk.go_to_local_point(0, 0, 1.5, 0)
    time.sleep(5)
    mk.go_to_local_point(1, 0, 1.5, 0)
    time.sleep(5)
    mk.go_to_local_point(0.125, -0.625, 1.5, 0)
    time.sleep(5)
    mk.go_to_local_point(0.5, 0.375, 1.5, 0)
    time.sleep(5)
    mk.go_to_local_point(0.875, -0.625, 1.5, 0)
    time.sleep(5)
    mk.go_to_local_point(0, 0, 1.5, 0)
    time.sleep(5)
finally:
    mk.land()
    time.sleep(2)
    mk.disarm()