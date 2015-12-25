import cv2
import numpy as np


img = cv2.imread('10.jpg')
newImage=np.zeros(img.shape,np.uint8)
gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

i, j, k = img.shape

for x in xrange(i):
  for y in xrange(j):
    R = img[x,y,2] * 0.256 + img[x,y,1] * 0.145 + img[x,y,0] * 0.342
    G = img[x,y,2] * 0.349 + img[x,y,1] * 0.686 + img[x,y,0] * 0.168
    B = img[x,y,2] * 0.272 + img[x,y,1] * 0.534 + img[x,y,0] * 0.131
    if R > 255:
        newImage[x,y,2] = 255
    else:
        newImage[x,y,2] = R
    if G > 255:
        newImage[x,y,1] = 255
    else:
        newImage[x,y,1] = G
    if B > 255:
        newImage[x,y,0] = 255
    else:
        newImage[x,y,0] = B

cv2.imwrite('/home/vishnu/sepia_bw/12.jpg',newImage)
cv2.imwrite('/home/vishnu/sepia_bw/13.jpg',gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
