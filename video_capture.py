import cv2 

# load image
img = cv2.imread('Thinking-of-getting-a-cat.png')
#print(img)

# load img from webCam
capture_img = cv2.VideoCapture(0) # define camera
# start

status_camera,img = capture_img.read() # start camera to take picture

print(status_camera)
print(img)
# while True:


#     # to show img
#     # cv2.imshow('Thinking-of-getting-a-cat.png',img) # imgshow(window_name,img_data)

#     cv2.imshow('Live',img)

#     # hold window
#     if cv2.waitKey(30) & 0xff == 'q': # infinte loop times open window
#         break


