import cv2

# now loading camera driver
cap = cv2.VideoCapture(0)
#loading face data
face_detect = cv2.CascadeClassifier('face.xml')
eye_detect = cv2.CascadeClassifier('eye.xml')
print(dir(face_detect))

while cap.isOpened():
    # taking picture
    status, frame = cap.read()
    # converting into gray
    grayimg = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    print(grayimg)
    # now Detect face
    face = face_detect.detectMultiScale(grayimg)
    print(face)
    for  (x,y,w,h) in face:
	    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),4)
        only_face = frame[y:y+h,x:x+w]
        eye = eye_detect.detectMultiScale(only_face)
        for (ex,ey,ew,eh) in eye:
            cv2.rectangle(only_face,(ex,ey),(ex+ew,ey+eh),(255,0,0),2)
    cv2.imshow('face',frame)
    if cv2.waitKey(10) & 0xff == ord('q'):
        break

# to destroy all window by imshow
cv2.destroyAllWindows()
cap.release()


