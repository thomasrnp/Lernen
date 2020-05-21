import cv2
import numpy as np
print("CV version: ", cv2.__version__)
cv2.namedWindow('Kamera')

img1=np.zeros((480, 640, 1), np.uint8)
img1[0:480,0:320] = [255]

img2=np.zeros((480, 640, 1), np.uint8)
img2[190:290,270:370] = [255]

bitAnd = cv2.bitwise_and(img1, img2)

cam = cv2.VideoCapture(0)

while True:
    ret, frame=cam.read()
    cv2.imshow('Kamera', frame)
    cv2.moveWindow('Kamera',0,0)

    cv2.imshow('img1', img1)
    cv2.moveWindow('img1', 0, 500)

    cv2.imshow('img2', img2)
    cv2.moveWindow('img2', 700, 0)

    cv2.imshow('bitAnd', bitAnd)
    cv2.moveWindow('bitAnd', 700, 500)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows


