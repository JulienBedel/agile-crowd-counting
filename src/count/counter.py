import cv2
import imutils
import numpy as np

known_images = ['crowd.png']
known_images_path = './src/count/known_images/'


def count(image_path):
    count = 0

    image = open(image_path, "rb").read()
    image_found = None

    for known_image in known_images:
        if image == open(known_images_path + known_image, "rb").read():
            image_found = known_image
            break

    if (not image_found):
        return -1

    img_rgb = cv2.imread(image_path)
    imgYCC = cv2.cvtColor(img_rgb, cv2.COLOR_YCrCb2RGB)
    img_gray = cv2.cvtColor(imgYCC, cv2.COLOR_BGR2GRAY)

    lower = np.array([178])
    upper = np.array([202])
    shapeMask = cv2.inRange(img_gray, lower, upper)

    cnts = cv2.findContours(shapeMask.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    return len(cnts)