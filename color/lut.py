import cv2
import numpy as np
import os
from efe import add_effect
pat='/home/vishnu/working_dir/express/'
dirs=os.listdir(pat)
imlist=[filename for filename in dirs if  filename[-4:] in [".jpg",".JPG"]]


for x in range(0,len(imlist)):
 img=cv2.imread(pat+imlist[x])
 
 img2=cv2.imread("accept.jpg")
 img2=cv2.resize(img2,(512,512))
 lt0 = np.zeros((1,256), np.uint8)
 lt1 = np.zeros((1,256), np.uint8)
 lt2 = np.zeros((1,256), np.uint8)

 for j in range(0,256):

    lt0[0,j]=img[...,0][0,j]
    lt1[0,j]=img[...,1][0,j]
    lt2[0,j]=img[...,2][0,j]

 img2[...,0] = cv2.LUT(img2[...,0], lt0)
 img2[...,1] = cv2.LUT(img2[...,1], lt1)
 img2[...,2] = cv2.LUT(img2[...,2], lt2)
 
 cv2.imwrite("/home/vishnu/working_dir/"+imlist[x],img2)
