import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('Camera open failed')
    exit()

while True:
    ret, frame = cap.read()
    frame2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame3 = cv2.Canny(frame, 100, 150)  

    if not ret:
        break 

    cv2.imshow('frame', frame)
    cv2.imshow('black', frame2)
    cv2.imshow('edge', frame3)


    if cv2.waitKey(10) == 27:
        break


#ret, frame = cap.read()
#cv2.imwrite('output.jpg', frame)
#cv2.imshow('frame', frame)
#cv2.waitKey(0)

cap.release()
cv2.destroyAllWindows()