import cv2
from pioneer_sdk import *

mk=Pioneer()
cam=Camera()
while True:
    img=cam.get_cv_frame()
    cv2.imshow("name", img)
    if cv2.waitKey(1) == ord("q"):
        break