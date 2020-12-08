#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 09:40:34 2020

@author: looser
"""

import cv2
import numpy as np
from time import sleep
from apple2 import greenapple
def nothing():
    pass

a=0
b=0
c=0
d=0
e=0
f=0
g=0
h=0
i=0
j=0
    

import os
import glob

file="/home/looser/Desktop/Project materials/New folder (3)/New folder/"
    
    
data_path = os.path.join(file,'*g')
files = glob.glob(data_path)
    
for f1 in files:
    img = cv2.imread(f1)
    frame = cv2.resize(img, (500,500))
    ilowH = 0
    ihighH = 16

    ilowS = 0
    ihighS = 255
    ilowV = 0
    ihighV = 255
    
    
    blurred = cv2.GaussianBlur(frame, (5, 5), 0)
    ima=cv2.cvtColor(blurred,cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)    
    lower_hsv = np.array([ilowH, ilowS, ilowV])
    higher_hsv = np.array([ihighH, ihighS, ihighV])
    mask = cv2.inRange(hsv, lower_hsv, higher_hsv)
    kernal =np.ones((5,5), np.uint8)
    mask=cv2.erode(mask,kernal)
    cv2.imshow("frame",mask)
    res=cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow("res",mask)
    countRed = cv2.countNonZero(mask)
    print(countRed)
    sleep(2)
    if countRed > 30000: #choose whatever condition you want
        print("red apple found and now checking for fresh or rotten")
        sleep(2)
        ilowH1 = 0
        ihighH1 = 16

        ilowS1 = 73
        ihighS1 = 255
        ilowV1 =140
        ihighV1 = 255
        
        lower_hsv1 = np.array([ilowH1, ilowS1, ilowV1])
        higher_hsv1 = np.array([ihighH1, ihighS1, ihighV1])
        mask1 = cv2.inRange(hsv, lower_hsv1, higher_hsv1)
        kernal1 =np.ones((5,5), np.uint8)
        mask1=cv2.erode(mask1,kernal1)
        cv2.imshow("frame1",mask1)
        res1=cv2.bitwise_and(frame,frame,mask=mask1)
        cv2.imshow("res1",res1)
        countrotten=cv2.countNonZero(mask1)
        print(countrotten)
        
        if  countrotten>10000 :
            print("freshapple found")
            
            c=c+1
            
        else :
            print('rotten apple ')
            
            d=d+1
           
    else :
      (a,j)=greenapple(frame)
      if (a+j)==0:
          print("apples that couldnot pass")
          h=h+1
      else:
          f=f+a
          g=g+j
          
        
    cv2.waitKey(10)
    print("Image Saved")
    print("Program End")
    b=c+d
    e=f+g
    i=b+e+h
    print('number of red apple',b)
    
    print('freshapples=',c) 
   
    print('rottenapples=',d)
    
    print('number of green =',e)
    
    print('freshgreenapples=',f) 
   
    print('rottengreenapples=',g)
    
    print('apples that couldnot pass',h)
    
    print('total no.of apples=',i)
    
    if cv2.waitKey(100) & 0xFF==ord('q'):
        break
        

cv2.destroyAllWindows()