import cv2 

# load image
img = cv2.imread('Thinking-of-getting-a-cat.png')
#print(img)

# load img from webCam
capture_img = cv2.VideoCapture(0) # define camera
# start
status_camera,img = capture_img.read() # start camera to take picture


# check type data
print(type(img))

# to check row and column
print(img.shape)

# crop image
croped_img = img[0:550,200:900]
# cv2.imshow('Thinking-of-getting-a-cat.png',croped_img) # imgshow(window_name,img_data)

# draw rectangle on img
cv2.rectangle(img,(0,0),(100,200),(0,0,255),-1)

# draw line on img
cv2.line(img,(0,0),(100,200),(255,0,255),2)
# cv2.line(imge,first_cord,sec_cord,color,width_of_Line)

# draw circle on img
cv2.circle(img,(100,200),50,(255,255,255),2)



cv2.imshow('img',img)

# to show img
# cv2.imshow('Thinking-of-getting-a-cat.png',img) # imgshow(window_name,img_data)

# hold window
cv2.waitKey(0) # infinte loop times open window



