import cv2

cap=cv2.VideoCapture(0)

while True:
    rf, frame=cap.read()
    cv2.imshow("name", frame)
    if cv2.waitKey(1)==ord("q"):
        break