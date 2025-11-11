import cv2, pioneer_sdk

cam=pioneer_sdk.Camera()
mk=pioneer_sdk.Pioneer()

img=cam.get_cv_frame()

while True:
    img=cam.get_cv_frame()
    flipx=cv2.flip(img, 0)
    flipy=cv2.flip(img, 1)
    flipxy=cv2.flip(img, -1)
    cv2.imshow('name', cv2.vconcat([cv2.hconcat([img, flipy]), cv2.hconcat([flipx, flipxy])]))
    keey=cv2.waitKey(1)
    if keey==27 or keey==ord('q'):
        break