from pioneer_sdk import *
import time

mk=Pioneer()
mk.arm()
time.sleep(1)
mk.takeoff()
try:
    time.sleep(2)
    mk.go_to_local_point_body_fixed(0, 1, 0, 0)
    time.sleep(2)
    mk.go_to_local_point_body_fixed(1, 0, 0, -3,14/2)
    time.sleep(2)
    mk.go_to_local_point_body_fixed(0, -1, 0, -3,14/2)
    time.sleep(2)
    mk.go_to_local_point_body_fixed(-1, 0, 0, -3,14/2)
    time.sleep(2)
finally:
    mk.land()
    time.sleep(2)
    mk.disarm()