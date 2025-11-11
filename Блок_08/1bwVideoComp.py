import cv2

cam=cv2.VideoCapture(0)
while True:
    r, img = cam.read()
    img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('name', img)
    keey=cv2.waitKey(1)
    if keey==ord('q') or keey==27:
        break