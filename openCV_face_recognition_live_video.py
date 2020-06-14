import face_recognition
import cv2
import os
import pickle
print("cv2 version: ", cv2.__version__)
print("face_recognition version: ", face_recognition.__version__)

Encodings=[]
Names=[]

with open('train.pkl', 'rb') as f:
    Names = pickle.load(f)
    Encodings = pickle.load(f)

# cam = cv2.VideoCapture(0)
cam = cv2.VideoCapture('/home/fred/Videos/Thomas.mp4')

# Check if camera opened successfully
if (cam.isOpened()== False): 
    print("Error opening video stream or file!")

font=cv2.FONT_HERSHEY_SIMPLEX

while (cam.isOpened()):
    ret, frame=cam.read()
    frameSmall = cv2.resize(frame, (0,0), fx=.33, fy=.33)
    frameRGB = cv2.cvtColor(frameSmall, cv2.COLOR_BGR2RGB)
    facePositions = face_recognition.face_locations(frameRGB,model='hog')
    # facePositions = face_recognition.face_locations(frameRGB,model='cnn')
    allEncodings = face_recognition.face_encodings(frameRGB, facePositions)
    for (top, right, bottom, left),face_encoding in zip(facePositions, allEncodings):
        name = 'Unknown Person'
        matches = face_recognition.compare_faces(Encodings, face_encoding)
        if True in matches:
            first_match_index = matches.index(True)
            name = Names[first_match_index]

        top = top*3
        right = right*3
        bottom = bottom*3
        left=left*3    
        
        cv2.rectangle(frame, (left, top),(right, bottom), (0,0,255), 2)
        cv2.putText(frame, name, (left, top-6), font, 1, (0,0,255))
    
    cv2.imshow('Picture', frame)
    cv2.moveWindow('Picture', 10, 10)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows

