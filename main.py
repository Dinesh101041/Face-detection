from cv2 import cv2 

# readint the image
orgimage=cv2.imread('./images/wc.jpg')

# covert image into a gray scale
grayimg=cv2.cvtColor(orgimage, cv2.COLOR_BGR2GRAY)

# load the viola-jones classifier-object detection framework
face_cascade = cv2.CascadeClassifier('./classifier\haarcascade_frontalface_alt.xml')

# mulitiscale() - to get a image as arugument to classify image
face_detct=face_cascade.detectMultiScale(grayimg)

# draw a rectangle amomg images
for (column,row,width,height) in face_detct:
    cv2.rectangle(
        orgimage,
        (column,row),
        (column + width, row + height),
        (0,255,0),
        2
    )


# displayin image
cv2.imshow('image',orgimage)
# wait until key stroke to close the image
cv2.waitKey(0)
# closing the image
cv2.destroyAllWindows()
