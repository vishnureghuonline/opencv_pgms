import cv2
import numpy as np
from efe import add_effect
import sys
from PIL import ImageEnhance
from light import get_light
import Image


img = cv2.imread("4613041807174166162.jpg")
im=np.copy(img)
newImage=np.zeros(img.shape,np.uint8)
img = cv2.fastNlMeansDenoisingColored(img,None,5,5,5,21)
i, j, k = img.shape

R = img[...,2] * 1.0 + img[...,1] * 0.0+ img[...,0] * 0.0
G = img[...,2] * 0.5+ img[...,1] * 1.0 + img[...,0] * 0.0
B = img[...,2] * 0.5 + img[...,1] * 0.0 + img[...,0] * 1.0
R[R>255]=255
G[G>255]=255
B[B>255]=255
newImage[...,2] =R
newImage[...,1] =G
newImage[...,0] =B

im_pil = Image.fromarray(newImage)
sharp= ImageEnhance.Contrast(im_pil)#0.0-1.0
dst=sharp.enhance(1.8)
color= ImageEnhance.Color(dst)#0.0-1.0
dst=color.enhance(0.5)

#bright= ImageEnhance.Brightness(dst)#0.0-1.0
#dst=bright.enhance(1.2)


pix=np.array(dst)
#pix=get_light(pix)
enhanced_image= cv2.addWeighted(pix,0.3,img,0.5, 0)
cv2.imshow("real",im)
cv2.imshow("effect1",enhanced_image)
cv2.imwrite("final2.jpg",enhanced_image)
"""

img = cv2.imread("4613041807174166162.jpg")
im=np.copy(img)
newImage=np.zeros(img.shape,np.uint8)
img = cv2.fastNlMeansDenoisingColored(img,None,5,5,5,21)
i, j, k = img.shape

R = img[...,2] * 0.1 + img[...,1] * 0.3+ img[...,0] * 0.3
G = img[...,2] * 0.3 + img[...,1] * 0.3 + img[...,0] * 0.4
B = img[...,2] * 0.3 + img[...,1] * 0.3 + img[...,0] * 0.4
R[R>255]=255
G[G>255]=255
B[B>255]=255
newImage[...,2] =R
newImage[...,1] =G
newImage[...,0] =B

im_pil = Image.fromarray(newImage)
sharp= ImageEnhance.Sharpness(im_pil)#0.0-1.0
dst=sharp.enhance(1.9)

pix=np.array(dst)

enhanced_image= cv2.addWeighted(pix,0.5,img,0.5, 0)
cv2.imshow("real",img)
cv2.imshow("effect2",enhanced_image)



img = cv2.imread("4613041807174166162.jpg")
im=np.copy(img)
newImage=np.zeros(img.shape,np.uint8)
img = cv2.fastNlMeansDenoisingColored(img,None,5,5,5,21)
i, j, k = img.shape

R = img[...,2] * 1.0 + img[...,1] * 0.3+ img[...,0] * 0.6
G = img[...,2] * 0.0 + img[...,1] * 1.0 + img[...,0] * 0.0
B = img[...,2] * 0.3 + img[...,1] * 0.3 + img[...,0] * 1.0
R[R>255]=255
G[G>255]=255
B[B>255]=255
newImage[...,2] =R
newImage[...,1] =G
newImage[...,0] =B

im_pil = Image.fromarray(newImage)
sharp= ImageEnhance.Sharpness(im_pil)#0.0-1.0
dst=sharp.enhance(1.4)

pix=np.array(dst)

enhanced_image= cv2.addWeighted(pix,0.5,img,0.5, 0)
cv2.imshow("real",img)
cv2.imshow("effect3",enhanced_image)
"""
cv2.waitKey(0)
