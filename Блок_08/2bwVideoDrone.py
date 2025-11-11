import cv2
import pioneer_sdk

mk=pioneer_sdk.Pioneer()
cam=pioneer_sdk.Camera()

while True:
    img = cam.get_cv_frame()
    img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('name', img)
    keey=cv2.waitKey(1)
    if keey==ord('q') or keey==27:
        break