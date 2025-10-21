import cv2

img=cv2.imread("image1.jpg")
cv2.imshow("name", img)
while True:
    if cv2.waitKey(-1) == ord("q"):
        break