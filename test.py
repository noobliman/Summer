import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('C:\\Users\\Liman\\AppData\\Local\\Programs\\Python\\Python36-32\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml')
video_capture = cv2.VideoCapture(0)
while True:
    ret, img = video_capture.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
    cv2.imshow('Video', img)
    k=cv2.waitKey(1)
    if(k==27):
    	break
video_capture.release()
cv2.destroyAllWindows()