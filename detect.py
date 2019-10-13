# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 07:32:45 2019

@author: 91811
"""

import cv2
face_cascade= cv2.CascadeClassifier('C:\\Users\\91811\\opencv\\build\\etc\\haarcascades\\haarcascade_frontalface_default.xml')
img= cv2.imread('imggg.jfif')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale( gray,scaleFactor=1.5,minNeighbors=4,minSize=(30, 30))
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
cv2.imshow("Faces found", img)
cv2.waitKey(0)




