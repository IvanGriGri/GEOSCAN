from pioneer_sdk import *
import time

mk=Pioneer()
mk.arm()
time.sleep(1)
mk.takeoff()
try:
    mk.go_to_local_point(0, 0, 1, 0)
    time.sleep(5)
    mk.go_to_local_point(0, 1, 1, 0)
    time.sleep(5)
    mk.go_to_local_point(1, 1, 1, 0)
    time.sleep(5)
    mk.go_to_local_point(1, 0, 1, 0)
    time.sleep(5)
    mk.go_to_local_point(0, 0, 1, 0)
    time.sleep(5)
finally:
    mk.land()
    time.sleep(5)
    mk.disarm()