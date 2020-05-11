import cv2
import imutils
import numpy as np
from matplotlib import pyplot as plt

img_rgb = cv2.imread('crowd.png')
imgYCC = cv2.cvtColor(img_rgb, cv2.COLOR_YCrCb2RGB)
img_gray = cv2.cvtColor(imgYCC, cv2.COLOR_BGR2GRAY)


##################
lower = np.array([178])
upper = np.array([202])
shapeMask = cv2.inRange(img_gray, lower, upper)

cnts = cv2.findContours(shapeMask.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
#cv2.imshow("Mask", shapeMask)

##################



cv2.imwrite('res.png',img_rgb)
cv2.imwrite('test.png', imgYCC)
cv2.imwrite('test2.png', img_gray)
cv2.imwrite('test22.png', shapeMask)
#cv2.imwrite('test4.png', imgYCC2)

if len(cnts) == 0:
    print(-1)
else :
    print(len(cnts))



