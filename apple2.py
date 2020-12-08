#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 09:44:29 2020

@author: looser
"""

import cv2
import numpy as np
from time import sleep



def greenapple(frame) :
    f=0
    g=0
    ilowH2 = 16
    ihighH2 = 70

    ilowS2 = 25
    ihighS2 = 255
    ilowV2 = 0
    ihighV2 = 255
    blurred = cv2.GaussianBlur(frame, (5, 5), 0)
    
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)    
    lower_hsv = np.array([ilowH2, ilowS2, ilowV2])
    higher_hsv = np.array([ihighH2, ihighS2, ihighV2])
    mask2 = cv2.inRange(hsv, lower_hsv, higher_hsv)
    kernal =np.ones((5,5), np.uint8)
    mask3=cv2.erode(mask2,kernal)
    cv2.imshow("frame",mask3)
    res3=cv2.bitwise_and(frame,frame,mask=mask3)
    cv2.imshow("res",res3)
    countgreen = cv2.countNonZero(mask3)
    print(countgreen)
    sleep(2)
    if countgreen > 6000: #choose whatever condition you want
        print("green apple found")
        print("Now checking for green fresh or rotten found")
            
        ilowH1 = 16
        ihighH1 = 70
        ilowS1 = 25
        ihighS1 = 255
        ilowV1 =130
        ihighV1 = 255
        
        lower_hsv1 = np.array([ilowH1, ilowS1, ilowV1])
        higher_hsv1 = np.array([ihighH1, ihighS1, ihighV1])
        mask4 = cv2.inRange(hsv, lower_hsv1, higher_hsv1)
        kernal1 =np.ones((5,5), np.uint8)
        mask5=cv2.erode(mask4,kernal1)
        cv2.imshow("frame1",mask5)
        res2=cv2.bitwise_and(frame,frame,mask=mask2)
        cv2.imshow("res1",res2)
        countgreenrotten=cv2.countNonZero(mask2)
        print(countgreenrotten)
        
        if  countgreenrotten>(countgreen-2000) :
                print("fresh greenapple found")
                f=f+1
                
        else :
                print('rotten apple ')
                g=g+1
    return(f,g)