import cv2
import numpy as np

cascade = '../models/haarcascade_frontalface_alt.xml'



def face_detector(img):
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(
        gray,
        scaleFactor=1.15,
        minNeighbors=5,
        minSize=(5, 5),
        flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+w),(0,255,0),2)

        cv2.circle(img, ((x + x + w) / 2, (y + y + h) / 2), w / 2, (0, 255, 0), 2)

    return img

path =
img = cv2.imread('')