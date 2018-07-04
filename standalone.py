import os
import time
import sys
import urllib
import numpy as np
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
opn=int(input("\nChoose an option :\n1. Enter image detection mode.\n2. Enter video detection mode.\n\n"))
face_cascade = cv2.CascadeClassifier('/usr/share/opencv/haarcascades/haarcascade_frontalface_default.xml')
st=str(sys.version)
if(opn==1):
	pat=int(input("\nChoose one:\n1.Enter address/url of picture with extention.\n2.Enter 0 to use webcam.\n\n"))
	if pat!=0:
		pat=int(input("\nChoose one:\n1.Enter the local address of picture with extention.\n2.Enter the url of image.\n\n"))
		if(pat==2):
			if(st[0]=='2'):
				uuu=input("\nEnter the url within quotes:\n\n")
				req = urllib.urlopen(uuu)
			else:
				uuu=input("\nEnter the url:\n\n")
				req = urllib.request.urlopen(uuu)
			arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
		else:
			if(st[0]=='2'):
				uuu=input("\nEnter the local address within quotes:\n\n")
			else:
				uuu=input("\nEnter the local address:\n\n")			
			x=os.path.normpath(uuu)
	else:
		x=0;
		print("\nSmile,your picture is being taken.\n")
		time.sleep(1)
		print(":)\n")
		time.sleep(1)
	if pat==0:
		video_capture = cv2.VideoCapture(x)
		ret, img = video_capture.read()
		video_capture.release()
	else:
		if pat==2:
			img = cv2.imdecode(arr, -1)
		else:
			img = cv2.imread(x)
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
	if st[0]=='3':
		pat=int(input("\nChoose one:\n1.Enter address of video with extention.\n2.Enter 0 to use webcam.\n\n"))
	else:
		pat=int(input("\nChoose one:\n1.Enter address/url of video with extention.\n2.Enter 0 to use webcam.\n\n"))
	if pat!=0:
		if(st[0]=='3'):
			pat=input("\nEnter the address of video with extention:\n\n")
		else:
			pat=input("\nEnter the address/url of video with extention within quotes:\n\n")
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
