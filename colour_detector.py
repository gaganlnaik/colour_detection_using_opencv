# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Function which counts number of red pixels in the image
def red_pixels_counter(i):
    lower=np.array([0,0,100],dtype="uint8")
    upper=np.array([50,50,255],dtype="uint8")
    mask1=cv2.inRange(i,lower,upper)
#To see an image where red pixels are converted to white and other pixels to black
    #cv2.imshow('red_pixels',mask1)
    number_red=np.sum(mask1==255)
    return number_red


#Function which counts number of green pixels in the image
def green_pixels_counter(i):
    lower=np.array([0,100,0],dtype="uint8")
    upper=np.array([60,255,50],dtype="uint8")
    mask2=cv2.inRange(i,lower,upper)
#To see an image where green pixels are converted to white and other pixels to black
    #cv2.imshow('green_pixels',mask2)
    number_green=np.sum(mask2==255)
    return number_green


#Function which counts number of blue pixels in the image
def blue_pixels_counter(i):
    lower=np.array([100,0,0],dtype="uint8")
    upper=np.array([255,110,50],dtype="uint8")
    mask3=cv2.inRange(i,lower,upper)
#To see an image where blue pixels are converted to white and other pixels to black
    cv2.imshow('blue_pixels',mask3)
    number_blue=np.sum(mask3==255)
    return number_blue


#Function which counts number of yellow pixels in the image
def yellow_pixels_counter(i):
    lower=np.array([0,100,100],dtype="uint8")
    upper=np.array([70,255,255],dtype="uint8")
    mask4=cv2.inRange(i,lower,upper)
#To see an image where yellow pixels are converted to white and other pixels to black
    #cv2.imshow('yellow_pixels',mask4)
    number_yellow=np.sum(mask4==255)
    return number_yellow
    

import cv2
import numpy as np
#List where first element represents number of red pixels, second green, third blue and fourth yellow
colours_pixel_list=[0,0,0,0]
#Give the name of the image which you want to check
img1=cv2.imread('blue_cube.jpg')
cv2.imshow('original_image',img1)
colours_pixel_list[0]=red_pixels_counter(img1)
colours_pixel_list[1]=green_pixels_counter(img1)
colours_pixel_list[2]=blue_pixels_counter(img1)
colours_pixel_list[3]=yellow_pixels_counter(img1)

print(colours_pixel_list)

#To find which colour pixels are present in highest number 
maximum=0
index=0
for i,value in enumerate(colours_pixel_list):
    if value>maximum:
        maximum=value
        index=i

if index==0:
    print('red')
elif index==1:
    print('green')
elif index==2:
    print('blue')
else:
    print('yellow')


    
        
cv2.waitKey(100000)
cv2.destroyAllWindows()
