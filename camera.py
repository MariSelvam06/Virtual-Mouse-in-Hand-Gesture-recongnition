import cv2
cap = cv2.VideoCapture("http://192.168.43.1:8080/video")
while True:
    ret, frame = cap.read()
    resized = cv2.resize(frame, (640, 420))
    cv2.imshow("Frame", resized)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
