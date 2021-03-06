import cv2

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('./xml/face.xml')

if not cap.isOpened():
    print('Camera open failed')
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        break 

    faces = face_cascade.detectMultiScale(frame,1.3,5)
    for(x,y,w,h) in faces:
	    cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    
    cv2.imshow('frame', frame)

    if cv2.waitKey(10) == 27:
        break

cap.release()
cv2.destroyAllWindows()