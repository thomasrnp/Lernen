import cv2

# dispW = 920
# dispH = 760

cam = cv2.VideoCapture(0)
# cam.set(cv2.CAP_PROP_FRAME_WIDTH, dispW)
# cam.set(cv2.CAP_PROP_FRAME_HEIGHT, dispH)

while True:
    ret, frame=cam.read()
    cv2.imshow('Kamera', frame)
    cv2.moveWindow('Kamera', 1100, 0)
    
    frameSmall=cv2.resize(frame,(320,240))
    cv2.imshow('KameraSmall', frameSmall)
    cv2.moveWindow('KameraSmall', 0, 0)
    
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    graySmall=cv2.resize(gray, (320,240))
    cv2.imshow('BW', graySmall)
    cv2.moveWindow('BW', 0, 320)
   
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows