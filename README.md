# Face-Filter
Basic face filter app coded in python using OpenCV

This program opens an interface that will display your webcam footage, detect your face, and allow you to apply different "filters" to it, which can be changed with the on screen buttons. This is done using a combination of TKInter's helpful interface tools and OpenCV's computer vision/face detection. Both libraries are very straightforward to use, but I found combining them caused some trouble to be able to properly overlay images onto the user's face.

To install and run the project, download all the files into the same directory and run the python file. Make sure to have opencv downloaded and a webcam plugged in/active to avoid potential errors. The face detector will only detect frontal faces, and may not work in environments too bright or dark.

The haarcascade_frontalface_default.xml file was not made by me. It was acquired from OpenCV's library (https://github.com/opencv/opencv/tree/master/data/haarcascades).
The images in the project do not belong to me, and were all taken from google images.
