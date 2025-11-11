from pioneer_sdk import *
import cv2, time

step=0.5

mk=Pioneer()
cam=Camera()
t=0
mk.arm()
mk.takeoff()
try:
    mk.go_to_local_point_body_fixed(0, 0, 1.5, 0)
    while True:
        key=cv2.waitKey(1)
        if key==ord("w"):
            mk.go_to_local_point_body_fixed(0, step, 0, 0)
        if key==ord("s"):
            mk.go_to_local_point_body_fixed(0, -1*step, 0, 0)
        if key==ord("a"):
            mk.go_to_local_point_body_fixed(-1*step, 0, 0, 0)
        if key==ord("d"):
            mk.go_to_local_point_body_fixed(step, 0, 0, 0)
        if key==ord("r"):
            mk.go_to_local_point_body_fixed(0, 0, step, 0)
        if key==ord("f"):
            mk.go_to_local_point_body_fixed(0, 0, -1*step, 0)
        if key==ord("h"):
            mk.go_to_local_point_body_fixed(0, 0, 0, 3.14/4)
        if key==ord("g"):
            mk.go_to_local_point_body_fixed(0, 0, 0, -3.14/4)
        if key==ord("q"):
            break
        if time.time()-t>2:
            t=time.time()
            print(mk.get_battery_status())
        img=cam.get_cv_frame()
        cv2.imshow("name", img)
finally:
    mk.land()