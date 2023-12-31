# -*- coding: utf-8 -*-
"""obj detection using YOLO.

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DS6RshA9emsYJtFuMIdKmMxjMI78o_ed

Cloning darknet repo , Darknet is a
Darknet is an open-source neural network framework written in C and CUDA. It is primarily designed for training and deploying deep neural networks for various computer vision tasks, including object detection and recognition.This framework has been trained on COCO dataset.
The COCO (Common Objects in Context) dataset is a widely used benchmark dataset for object detection, segmentation, and captioning. It consists of over 200,000 labeled images covering 80 different object categories.
After cloning this we can see the darknet folder in google collab files.
"""

!git clone https://github.com/pjreddie/darknet.git

"""Going into the darknet folder"""

cd darknet

"""ls command is used to see all the folders inside of it."""

ls

"""this command executes all the instructions which are there in the Makefile, which contains all the instructions required to setup YOLOv3."""

!make

"""Downloading the weights of YOLOv3 , weights is the all the parameters that the model has learned."""

!wget https://pjreddie.com/media/files/yolov3.weights

"""Displaying the image which i got from unsplash."""

import matplotlib.pyplot as plt
from PIL import Image

filename = "/content/darknet/data/my_image/zsun-fu-TL2e9aPgENs-unsplash.jpg"
image = Image.open(filename)
plt.imshow(image)
plt.axis('off')
plt.show()

"""executing this entire command to run infrencing on my image.

cfg/yolov3.cfg = YOLO architecture

yolov3.weights = YOLO weights

/content/darknet/data/my_imagezsun-fu-TL2e9aPgENs-unsplash.jpg = my image path
"""

!./darknet detect cfg/yolov3.cfg yolov3.weights /content/darknet/data/my_image/zsun-fu-TL2e9aPgENs-unsplash.jpg

"""This shows the ouptut image with bounding boxes around objects with their respective label."""

import matplotlib.pyplot as plt
from PIL import Image

filename = "/content/darknet/predictions.jpg"

image = Image.open(filename)
plt.imshow(image)
plt.axis('off')
plt.show()