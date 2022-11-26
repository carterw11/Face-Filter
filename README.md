# Face-Filter
A basic face filter app coded in python using OpenCV

## What is it?
This program opens an interface that will display your webcam footage, detect your face, and allow you to apply different "filters" to it, which can be changed with the on screen buttons. 

This is done using a combination of TKInter's helpful interface tools and OpenCV's computer vision/face detection. 

## How to run
To run the project, download all the files into the same directory and run the python file. 

The images I used for the project are potentially subject to copyright, so they have not been included on this repository. To make the images work, download a png of your choice under the names of happy, sad, angry, and sunglasses, and add them to the same directory as the python file.

Make sure to have opencv downloaded and a webcam plugged in/active to avoid potential errors. 

The face detector will only detect frontal faces, and may not work in environments too bright or dark.

## Credits
The haarcascade_frontalface_default.xml file was not made by me. It was acquired from OpenCV's library (https://github.com/opencv/opencv/tree/master/data/haarcascades).
