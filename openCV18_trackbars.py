import cv2
def nothing(n):
    pass

cam = cv2.VideoCapture(0)
cv2.namedWindow('Kamera')
cv2.createTrackbar('xVal', 'Kamera', 25,500,nothing)
cv2.createTrackbar('yVal', 'Kamera', 25,500,nothing)

while True:
    ret, frame=cam.read()
    xVal=cv2.getTrackbarPos('xVal','Kamera')
    yVal=cv2.getTrackbarPos('yVal','Kamera')
    # print(xVal, yVal)
    cv2.circle(frame, (xVal,yVal), 10, (255,0,0), -1)
    
    cv2.imshow('Kamera', frame)
    cv2.moveWindow('Kamera',0,0)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows


