import cv2

cam = cv2.VideoCapture(0)

while True:
    ret, frame=cam.read()
    cv2.imshow('Kamera', frame)
    cv2.moveWindow('Kamera',0,0)
    
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('GrayVideo', gray)
    cv2.moveWindow('GrayVideo',0,520)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows


