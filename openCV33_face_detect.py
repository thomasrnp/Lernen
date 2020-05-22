import cv2

cam = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier('cascades/face.xml')

while True:
    ret, frame=cam.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0),2)
    
    cv2.imshow('Kamera', frame)
    cv2.moveWindow('Kamera',0,0)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows


