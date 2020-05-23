import cv2
import face_recognition
print(cv2.__version__)

donFace = face_recognition.load_image_file('/home/fred/Documents/coding/Lernen/faceRecognizer/demoImages/known/Donald Trump.jpg')
donEncode = face_recognition.face_encodings(donFace)[0]

nancyFace = face_recognition.load_image_file('/home/fred/Documents/coding/Lernen/faceRecognizer/demoImages/known/Nancy Pelosi.jpg')
nancyEncode = face_recognition.face_encodings(nancyFace)[0]

Encodings = [donEncode, nancyEncode]
Names = ['The Donald', 'Nancy Pelosi']

font = cv2.FONT_HERSHEY_SIMPLEX
testImage = face_recognition.load_image_file('/home/fred/Documents/coding/Lernen/faceRecognizer/demoImages/unknown/u3.jpg')
facePostions = face_recognition.face_locations(testImage)
allEncodings = face_recognition.face_encodings(testImage, facePostions)

testImage = cv2.cvtColor(testImage, cv2.COLOR_RGB2BGR)

for (top, right, bottom, left), face_encoding in zip(facePostions, allEncodings):
    name = 'Unknown Person'
    matches = face_recognition.compare_faces(Encodings, face_encoding)
    if True in matches:
        first_match_index = matches.index(True)
        name = Names[first_match_index]
    cv2.rectangle(testImage, (left,top), (right, bottom), (0,0,255), 2)
    cv2.putText(testImage, name, (left, top-6), font, .75, (255,0,255), 1)

cv2.imshow('myWindow', testImage)
cv2.moveWindow('myWindow', 10, 10)

if cv2.waitKey(0) & 0xFF == ord('q'):
        cv2.destroyAllWindows