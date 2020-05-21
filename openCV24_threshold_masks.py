import cv2
import numpy as np

print("CV version: ", cv2.__version__)

dispW=320
dispH=240

cvLogo=cv2.imread('cv.jpg')
cvLogo=cv2.resize(cvLogo, (320,240))
cvLogoGray=cv2.cvtColor(cvLogo, cv2.COLOR_BGR2GRAY)
cv2.imshow('cvLogoGray', cvLogoGray)
cv2.moveWindow('cvLogoGray', 0, 350)

_,BGMask = cv2.threshold(cvLogoGray, 225, 255, cv2.THRESH_BINARY)
cv2.imshow('BG Mask',BGMask)
cv2.moveWindow('BG Mask', 385, 100)

FGMask = cv2.bitwise_not(BGMask)
cv2.imshow('FG Mask', FGMask)
cv2.moveWindow('FG Mask', 385, 350)

FG = cv2.bitwise_and(cvLogo, cvLogo, mask=FGMask)
cv2.imshow('FG', FG)
cv2.moveWindow('FG', 703, 350)

cv2.namedWindow('Kamera')
cam = cv2.VideoCapture(0)

while True:
    ret, frame=cam.read()
    frame=cv2.resize(frame,(320,240))

    BG = cv2.bitwise_and(frame, frame, mask = BGMask)
    cv2.imshow('BG', BG)
    cv2.moveWindow('BG', 703, 100)

    cv2.imshow('Kamera', frame)
    cv2.moveWindow('Kamera',0,10)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows


