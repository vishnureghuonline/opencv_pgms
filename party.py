import cv2
import numpy as np
from efe import add_effect
import sys
from PIL import ImageEnhance
import Image


img = cv2.imread("ambi.png")
newImage=np.zeros(img.shape,np.uint8)
img = cv2.fastNlMeansDenoisingColored(img,None,5,5,5,21)
i, j, k = img.shape

R = img[...,2] * 0.5 + img[...,1] * 0.3+ img[...,0] * 0.189
G = img[...,2] * 0.5 + img[...,1] * 0.3 + img[...,0] * 0.169
B = img[...,2] * 0.372 + img[...,1] * 0.3 + img[...,0] * 0.3
R[R>255]=255
G[G>255]=255
B[B>255]=255
newImage[...,2] =R
newImage[...,1] =G
newImage[...,0] =B
cv2.imshow("out",newImage)
cv2.waitKey(0)
cv2.imwrite("oo.jpg",newImage)
image=Image.open("oo.jpg")
sharp= ImageEnhance.Sharpness(image)#0.0-1.0
dst=sharp.enhance(1.9)
dst.save("final2.jpg")
