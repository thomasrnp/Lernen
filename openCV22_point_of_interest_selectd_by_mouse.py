import cv2
print("CV version: ", cv2.__version__)

goFlag = 0

def mouse_click(event,x,y,flags,parameters):
    global x1,y1,x2,y2
    global goFlag
    if event == cv2.EVENT_LBUTTONDOWN:
        x1 = x
        y1 = y
        goFlag = 0
    if event == cv2.EVENT_LBUTTONUP:
        x2 = x
        y2 = y
        goFlag = 1

cv2.namedWindow('Kamera')
cv2.setMouseCallback('Kamera', mouse_click)

cam = cv2.VideoCapture(0)

while True:
    ret, frame=cam.read()
    cv2.imshow('Kamera', frame)
    cv2.moveWindow('Kamera',0,0)

    if goFlag == 1:
        frame=cv2.rectangle(frame, (x1,y1),(x2,y2),(255,0,0),3)
        roi=frame[y1:y2,x1:x2]
        cv2.imshow('Copy ROI', roi)
        cv2.moveWindow('Copy ROI', 705, 0)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows


