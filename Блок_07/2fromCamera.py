import cv2

cap=cv2.VideoCapture(0)
rf, frame=cap.read()
cv2.imshow("name", frame)
while True:
    if cv2.waitKey(-1) == 27:
        break
cap.release()