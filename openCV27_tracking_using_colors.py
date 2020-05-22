import cv2

print(cv2.__version__)
import numpy as np
 
def nothing(x):
    pass
 
cv2.namedWindow('Trackbars')
cv2.moveWindow('Trackbars',1320,0)


# Setting to easily show a red object
cv2.createTrackbar('hueLower', 'Trackbars',152,179,nothing)
cv2.createTrackbar('hueUpper', 'Trackbars',179,179,nothing)
 
cv2.createTrackbar('hue2Lower', 'Trackbars',0,179,nothing)
cv2.createTrackbar('hue2Upper', 'Trackbars',0,179,nothing)
 
cv2.createTrackbar('satLow', 'Trackbars',135,255,nothing)
cv2.createTrackbar('satHigh', 'Trackbars',255,255,nothing)
cv2.createTrackbar('valLow','Trackbars',0,255,nothing)
cv2.createTrackbar('valHigh','Trackbars',255,255,nothing)

cam = cv2.VideoCapture(0)

while True:
    ret, frame=cam.read()
    frame = cv2.resize(frame,(320,240))
    cv2.imshow('Kamera', frame)
    cv2.moveWindow('Kamera', 0,0)

    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    hueLow=cv2.getTrackbarPos('hueLower', 'Trackbars')
    hueUp=cv2.getTrackbarPos('hueUpper', 'Trackbars')

    hue2Low=cv2.getTrackbarPos('hue2Lower', 'Trackbars')
    hue2Up=cv2.getTrackbarPos('hue2Upper', 'Trackbars')

    Ls=cv2.getTrackbarPos('satLow', 'Trackbars')
    Us=cv2.getTrackbarPos('satHigh', 'Trackbars')

    Lv=cv2.getTrackbarPos('valLow', 'Trackbars')
    Uv=cv2.getTrackbarPos('valHigh', 'Trackbars')

    l_b=np.array([hueLow,Ls,Lv])
    u_b=np.array([hueUp,Us,Uv])

    l_b2=np.array([hue2Low,Ls,Lv])
    u_b2=np.array([hue2Up,Us,Uv])

    FGmask=cv2.inRange(hsv,l_b,u_b)
    FGmask2=cv2.inRange(hsv,l_b2,u_b2)
    FGmaskComp=cv2.add(FGmask,FGmask2)
    cv2.imshow('FGmaskComp',FGmaskComp)
    cv2.moveWindow('FGmaskComp',0,530)

    FG=cv2.bitwise_and(frame, frame, mask=FGmaskComp)
    cv2.imshow('FG',FG)
    cv2.moveWindow('FG',700,0)

    bgMask=cv2.bitwise_not(FGmaskComp)
    cv2.imshow('bgMask',bgMask)
    cv2.moveWindow('bgMask',700,530)

    BG=cv2.cvtColor(bgMask,cv2.COLOR_GRAY2BGR)

    final=cv2.add(FG,BG)
    cv2.imshow('final',final)
    cv2.moveWindow('final',1400,0)

    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
