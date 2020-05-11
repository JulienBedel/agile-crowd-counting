import cv2
import numpy as np

import pathlib

known_images = ['crowd.png']
known_images_path = './src/count/known_images/'

def count(image_path):

    count = 0

    image = open(image_path,"rb").read()
    image_found = None

    for known_image in known_images:
        if image == open(known_images_path + known_image,"rb").read():
            image_found = known_image
            break
    
    if(not image_found):
        return -1 
    
    img = cv2.imread(image_path)
    imgYCC = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
    gray = cv2.cvtColor(imgYCC, cv2.COLOR_BGR2GRAY)

    print(known_images_path + 'template_{}'.format(image_found))
    template = cv2.imread((known_images_path + 'template_{}').format(image_found), 0)

    w, h = template.shape[::-1]

    res = cv2.matchTemplate(gray,template,cv2.TM_CCOEFF_NORMED)

    threshold = 0.77

    loc = np.where(res >= threshold)

    for pt in zip(*loc[::-1]):
        count = count + 1

    return count
