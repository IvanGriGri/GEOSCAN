import pioneer_sdk
import cv2
import time

mk=pioneer_sdk.Pioneer()
cam=pioneer_sdk.Camera()

img=cam.get_cv_frame()
h, w, ch = img.shape
q=time.time()
dist=None

while True:
    img=cam.get_cv_frame()
    if time.time()-q>0.2:
        dist=mk.get_dist_sensor_data()
        q=time.time()
    if not dist==None:
        cv2.putText(img, str(dist), [w-100, h-50], cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0))
        cv2.imshow('name', img)
    keey=cv2.waitKey(1)
    if keey==27 or keey==ord('q'):
        break