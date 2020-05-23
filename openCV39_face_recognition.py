import cv2
import face_recognition

print(cv2.__version__)

image = face_recognition.load_image_file('/home/fred/Documents/coding/Lernen/faceRecognizer/demoImages/unknown/u3.jpg')
face_locations = face_recognition.face_locations(image)
print(face_locations)
image=cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
for (row1, col1, row2, col2) in face_locations:
    cv2.rectangle(image, (col1, row1), (col2, row2), (0,0,255), 2)
cv2.imshow('myWindow', image)
cv2.moveWindow('myWindow', 10, 10)

if cv2.waitKey(0) & 0xFF == ord('q'):
        cv2.destroyAllWindows


