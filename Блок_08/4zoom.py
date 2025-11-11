import pioneer_sdk, cv2

mk=pioneer_sdk.Pioneer()
cam=pioneer_sdk.Camera()

img=cam.get_cv_frame()
h, w, ch=img.shape
x=w//4
y=h//4
x1=x + w//2
y1=y + h //2
cv2.imshow('zoom', img)
cv2.moveWindow('zoom', 700, 0)

while True:
    img=cam.get_cv_frame()
    img2=img[y:y1, x:x1].copy()
    cv2.rectangle(img, [x, y], [x1, y1], (255, 0, 0))
    img2 = cv2.resize(img2, [0, 0], fx=2, fy=2)
    cv2.imshow('original', img)
    cv2.imshow('zoom', img2)
    keey=cv2.waitKey(1)
    if keey==27 or keey==ord('q'):
        break