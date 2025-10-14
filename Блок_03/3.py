from pioneer_sdk import *
import time

mk=Pioneer()
mk.arm()
time.sleep(1)
mk.takeoff()
try:
    mk.go_to_local_point(0, 0, 1, 0)
    time.sleep(5)
    mk.go_to_local_point(0, 1, 1, -3.14/2)
    time.sleep(5)
    mk.go_to_local_point_body_fixed(0, 0, 0, -3,14/2)
    mk.go_to_local_point(1, 1, 1, -3.14)
    time.sleep(5)
    mk.go_to_local_point_body_fixed(0, 0, 0, -3,14)
    mk.go_to_local_point(1, 0, 1, -3.14*1.5)
    time.sleep(5)
    mk.go_to_local_point_body_fixed(0, 0, 0, -3,14*1.5)
    mk.go_to_local_point(0, 0, 1, -3.14*2)
    time.sleep(5)
finally:
    mk.land()
    time.sleep(5)
    mk.disarm()