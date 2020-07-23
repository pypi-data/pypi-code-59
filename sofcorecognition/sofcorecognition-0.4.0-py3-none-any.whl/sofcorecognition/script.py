#!/usr/bin/python
import numpy as np
import cv2
import face_recognition

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# import tensorflow as tf

def imcrop(img, bbox): 
    x1,y1,x2,y2 = bbox
    if x1 < 0 or y1 < 0 or x2 > img.shape[1] or y2 > img.shape[0]:
        img, x1, x2, y1, y2 = pad_img_to_fit_bbox(img, x1, x2, y1, y2)
    return img[y1:y2, x1:x2, :]

def run():
    img = cv2.imread("cemara.jpg")
    # img = cv2.rotate(img, cv2.ROTATE_90   _CLOCKWISE)
    # img = imcrop(img,(10,10,400,400))


    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imwrite("hasil.png", gray) 



    faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    # camera = cv2.VideoCapture(0);

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')


    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    print("Found {0} faces!".format(len(faces)))

    for (x, y, w, h) in faces:
        print(x)
        print(y)
        print(w)
        print(h)

        x1 = x
        x2 = x + w
        y1 = y
        y2 = y + h

        print("-----")
        croppedImage = imcrop(img,(x1,y1,x2,y2))
        croppedGrayImage = cv2.cvtColor(croppedImage, cv2.COLOR_BGR2GRAY)
        cv2.imwrite("face_{}.jpg".format(x1), croppedGrayImage) 
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("Faces found", img)
    cv2.waitKey(0)