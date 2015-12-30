import cv2
import numpy as np 
from enhance import*
from blur import*
# Read images
src = cv2.imread(sys.argv[1])
src = cv2.fastNlMeansDenoisingColored(src,None,5,5,5,21)
dst = np.copy(src)
mask = np.copy(src)
cv2.imshow("src",src)
edges = cv2.Canny(src,100,200)
mask[edges>0]=[0,0,0]
mask[edges==0]=[255,255,255]
dst=bright(dst,1.3)
dst=sharp(dst,1.9)
dst=sharp(dst,1.2)
width, height, channels = src.shape
center = (height/2, width/2)
output = cv2.seamlessClone(src, dst,mask, center, cv2.MIXED_CLONE)
output=blur_image(output)
cv2.imwrite("opencv-normal-clone-example.jpg",output)
cv2.imshow("dst",dst)
cv2.imshow("out",output)
cv2.waitKey(0)
