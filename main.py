import cv2 as cv

# readint the image
orgimage=cv.imread('./images/India.jpeg')

# covert image into a gray scale
grayimg=cv.cvtColor(orgimage, cv.COLOR_BGR2GRAY)

# load the viola-jones classifier-object detection framework
face_cascade = cv.CascadeClassifier('C:\Users\DINESH\anaconda3\Lib\site-packages\cv2\data\haarcascade_frontalface_alt.xml')

# mulitiscale() - to get a image as arugument to classify image
face_detct=face_cascade.detectMultiScale(grayimg)

# draw a rectangle amomg images
for (column,row,width,height) in face_detct:
    cv.rectangle(
        orgimage,
        (column,row),
        (column + widt, row + height),
        (0,255,0)
        2
    )


# displayin image
cv.imshow('image',orgimage)
# wait until key stroke to close the image
cv.waitLey(0)
# closing the image
cv.destroyAllWindows()
