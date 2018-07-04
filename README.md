# Summer Project
## Using ML and OpenCV for face recognition
### Last update : Bug fixes performed for standalone script

---

### Short method

#### Clong the directory

First and foremost you must clone the repository to your local storage.
You can either do it from the website or use git.
For using git run : `git clone https://github.com/noobliman/Summer` in the directory you want to clone.

#### Running face detecter

* Open terminal.
* Open project directory.
* Run either `python3 standalone.py` or `python standalone.py` as per your wish.

---

### Long method

Firstly we must ensure that these two are installed :

* Python
* Opencv

### Installing python

For windows just go to this [download link](https://www.python.org/downloads/) and choose a version.

### Installing Opencv 

#### For Windows

* Open Command Prompt.
* Go to C drive.
* Run : `pip install opencv-python`

#### For Ubuntu

##### *Pip* Method (easy)
* Open terminal
* Run the following commands :
  * `sudo apt-get install python-pip python-dev build-essential`
  * `sudo pip install --upgrade pip`
  * `sudo pip install --upgrade virtualenv`
  * `sudo apt-get install python3-pip`
  * `sudo apt-get install libopencv-dev python-opencv`
  * `sudo pip3 install opencv-python`
#### Building from source
>Note : This installed the unstable 4.0.0 version which wasn't able to work with my integrated webcam.
* Open terminal
* Step 1 : Update Ubuntu<br /><br />
`
sudo apt-get update
`
`
sudo apt-get upgrade
`

* Step 2 : Installing dependencies<br /><br/>
`
sudo apt-get install build-essential cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev
`

  `
sudo apt-get install python3-dev python3-numpy libtbb2 libtbb-dev
`

  `
sudo apt-get install libjpeg-dev libpng-dev libtiff5-dev libjasper-dev libdc1394-22-dev libeigen3-dev libtheora-dev libvorbis-dev libxvidcore-dev libx264-dev sphinx-common libtbb-dev yasm libfaac-dev libopencore-amrnb-dev libopencore-amrwb-dev libopenexr-dev libgstreamer-plugins-base1.0-dev libavutil-dev libavfilter-dev libavresample-dev
`

* Step 3 : Clone OpenCV<br /><br />
`
sudo -s
`

  `
cd /opt
`

  `
git clone https://github.com/opencv/opencv.git
`

  `
git clone https://github.com/opencv/opencv_contrib.git
`

* Step 4 : Build and Install.<br /><br />
`
cd opencv
`

  `
mkdir release
`

  `
cd release
`

  `
cmake -D BUILD_TIFF=ON -D WITH_CUDA=OFF -D ENABLE_AVX=OFF -D WITH_OPENGL=OFF -D WITH_OPENCL=OFF -D WITH_IPP=OFF -D WITH_TBB=ON -D BUILD_TBB=ON -D WITH_EIGEN=OFF -D WITH_V4L=OFF -D WITH_VTK=OFF -D BUILD_TESTS=OFF -D BUILD_PERF_TESTS=OFF -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D OPENCV_EXTRA_MODULES_PATH=/opt/opencv_contrib/modules /opt/opencv/
`

  `
make -j4
`

  `
make install
`

  `
ldconfig
`

  `
exit
`

You're done!



### Running the detecter

First and foremost you must clone the repository to your local storage.
You can either do it from the website or use git.
For using git run : `git clone https://github.com/noobliman/Summer` in the directory you want to clone.

#### For Windows :

>Note : Only one file is available for Windows which uses the Webcam to perform live face detection.However, it can be modified to use any video.

Simply open the test.py file to run it.

#### For Ubuntu :

>Note : Four files are available for Ubuntu.

##### For detecting faces from a live video captured using integrated webcam :

Open terminal in Summer directory and run `python3 test2.py`
##### For detecting faces from a downloaded video :

Open terminal in Summer directory and run `python3 Test_for_videoes.py`
Now simply enter the address of the file along with file extension to run.
>Example(for python 3) : /home/liman/Downloads/sample_vid.mp4

>Example(for python 2) : '/home/liman/Downloads/sample_vid.mp4'
<br />Remember to enter the address inside '' for python 2.



##### For detecting faces from a downloaded picture :

Open terminal in Summer directory and run `python3 Test_for_pictures.py`
Now simply enter the address of the file along with file extension to run.
>Example(for python 3) : /home/liman/Downloads/sample.png

>Example(for python 2) : '/home/liman/Downloads/sample.png'
<br />Remember to enter the address inside '' for python 2.


### The Face Detecter should be up and running without any issues.
---
