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
out=bright(img,1.3)
sharp=sharp(out,1.7)
out=contrast(out,1.6)
cv2.imshow("real",img)
cv2.imshow("effect1",out)
cv2.imwrite("final2.jpg",out)
cv2.waitKey(0)
