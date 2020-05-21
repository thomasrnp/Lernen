import cv2

cam = cv2.VideoCapture(0)

while True:
    ret, frame=cam.read()
    roi=frame[50:250, 200:400].copy()
    roiGray=cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

    # cv2.imshow('ROI', roi)
    # cv2.moveWindow('ROI', 705, 0)

    cv2.imshow('ROIGray', roiGray)
    cv2.moveWindow('ROIGray', 705, 0)

    cv2.imshow('Kamera', frame)
    cv2.moveWindow('Kamera',0,0)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows


