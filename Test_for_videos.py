import numpy as np
import cv2
import os

face_cascade = cv2.CascadeClassifier('/usr/share/opencv/haarcascades/haarcascade_frontalface_default.xml')
pat=input("Enter path (wrap \"\" for python2) of picture to be tested with file extention\n")
x=os.path.normpath(pat)
video_capture = cv2.VideoCapture(x)
while True:
    ret, img = video_capture.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
    cv2.imshow('Face Detecter', img)
    k=cv2.waitKey(1)
    if(k==27):
    	break
video_capture.release()
cv2.destroyAllWindows()
