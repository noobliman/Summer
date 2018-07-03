import os
import time
import sys
try:
	import pip
except ImportError:
	os.system("sudo apt-get install python-pip python-dev build-essential")
	os.system("sudo pip install --upgrade pip")
	os.system("sudo pip install --upgrade virtualenv")
	os.system("sudo apt-get install python3-pip")
try:
	import cv2
except ImportError:
	os.system("sudo apt-get install libopencv-dev python-opencv")
	os.system("sudo pip3 install opencv-python")
	import cv2
try:
	import numpy as np
except ImportError:
	os.system("sudo apt-get install python-numpy")
	os.system("sudo apt-get install python3-numpy")
	import numpy as np
opn=input("\nChoose an option :\n1. Enter image detection mode.\n2. Enter video detection mode.\n\n")
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
if(opn=='1'):
	pat=input("\nChoose one:\n1.Enter address/url of picture with extention.\n2.Enter 0 to use webcam.\n\n")
	if pat!='0':
		x=os.path.normpath(pat)
	else:
		x=0;
		print("\nSmile,your picture is being taken.\n")
		time.sleep(1)
		print(":)\n")
		time.sleep(1)
	imageSource = x
	if x!=0:
		img = cv2.imread(imageSource)
	else:
		video_capture = cv2.VideoCapture(x)
		ret, img = video_capture.read()
		video_capture.release()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	for (x, y, w, h) in faces:
	    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
	cv2.imshow('Face Detecter', img)
	while True:
	    k=cv2.waitKey(1)
	    if(k==27):
	    	break
	cv2.destroyAllWindows()
else:
	pat=input("\nChoose one:\n1.Enter address/url of video with extention.\n2.Enter 0 to use webcam.\n\n")
	if pat!='0':
		x=os.path.normpath(pat)
	else:
		x=0
		print("\nSmile,the camera is being switched on :\n")
		time.sleep(1)
		print(":)\n")
		time.sleep(1)
	print("Please hit the Esc button to end the runtime of the script.\nFace Detecter starting up in:\n")
	cntdwn=5
	while(cntdwn>0):
		sys.stdout.write(str(cntdwn))
		sys.stdout.flush()
		time.sleep(0.2)
		sys.stdout.write('.')
		sys.stdout.flush()
		time.sleep(0.2)
		sys.stdout.write('.')
		sys.stdout.flush()
		time.sleep(0.2)
		sys.stdout.write('.')
		sys.stdout.flush()
		print("\n")
		cntdwn=cntdwn-1
	sys.stdout.flush()
	print("\n")
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
