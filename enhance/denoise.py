import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('ambi.png')
dst = cv2.fastNlMeansDenoisingColored(img,None,5,5,5,21)
cv2.imshow("out",dst)
cv2.imshow("outd",img)
cv2.waitKey(0)
