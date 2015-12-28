#add effect of 0.3
import cv2
import numpy as np
from efe import add_effect
import sys
from PIL import ImageEnhance
from light import get_light
import Image
from blur import blur_image
from enhance import color,sharp,bright,contrast

img = cv2.imread("index.jpeg")
img = cv2.fastNlMeansDenoisingColored(img,None,5,5,5,21)
newImage=np.zeros(img.shape,np.uint8)
R = img[...,2] * 1.0 + img[...,1] * 0.0+ img[...,0] * 0.0
G = img[...,2] * 0.1+ img[...,1] * 1.0 + img[...,0] * 0.0
B = img[...,2] * 0.1 + img[...,1] * 0.0 + img[...,0] * 1.0
R[R>255]=255
G[G>255]=255
B[B>255]=255
newImage[...,2] =R
newImage[...,1] =G
newImage[...,0] =B

out=sharp(newImage,1.7)
out=contrast(out,1.3)
out=get_light(out)
cv2.imshow("real",img)
cv2.imshow("effect1",out)
cv2.imwrite("final2.jpg",out)
cv2.waitKey(0)
