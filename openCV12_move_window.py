import cv2

# cam = cv2.VideoCapture(0)
cam = cv2.VideoCapture('/home/fred/Videos/Thomas.mp4')

# Check if camera opened successfully
if (cam.isOpened()== False): 
    print("Error opening video stream or file!")

while(cam.isOpened()):
    ret, frame = cam.read()
    cv2.imshow('Kamera', frame)
    cv2.moveWindow('Kamera',0,0)
    
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('GrayVideo', gray)
    cv2.moveWindow('GrayVideo',0,520)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows


