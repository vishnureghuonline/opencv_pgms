import cv2
import sys 
refPt = []
cropping = False
#python mouse.py input.jpg/png..  
def click_and_crop(event, x, y, flags, param):
	if event == cv2.EVENT_LBUTTONDOWN:
		print image[x,y]


image = cv2.imread(sys.argv[1])
clone = image.copy()
cv2.namedWindow("image")
cv2.setMouseCallback("image", click_and_crop)
 
while True:
	cv2.imshow("image", image)
	key = cv2.waitKey(1) & 0xFF
 	if key == ord("c"):
		break
cv2.destroyAllWindows()
