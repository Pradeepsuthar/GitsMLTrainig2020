import  cv2
#  starting  camera
cap=cv2.VideoCapture(0)
# loading  haar file 
face_detect=cv2.CascadeClassifier('haarcascade_frontalcatface.xml')
#  to check drive loaded by python -- ans will true or false
#print(cap.isOpened())
# print(dir(face_detect))
while cap.isOpened():
	status,frame=cap.read()
#   converting  color image to gray scale 
	gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	#  now using  haar functions
	face=face_detect.detectMultiScale(gray)
	# print(face)
	for (x,y,w,h) in face:
		cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
	cv2.imshow('face',frame)
	if cv2.waitKey(10) & 0xff == ord('q'):
		break

cv2.destroyAllWindows()
cap.release()