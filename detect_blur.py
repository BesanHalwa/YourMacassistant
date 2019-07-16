"""
Select the most optimum picture for text conversion
---------------------------------------------------
Higher value of
cv2.Laplacian(image, cv2.CV_64F).var()
impiles more clarity

# TODO: check deconvolutional in cv2 for clearing the blur image
"""

import cv2
import glob


def ret_index()
    val_list = []

    for img in glob.iglob("temp/*.jpg"):

        image = cv2.imread(img)
        val = cv2.Laplacian(image, cv2.CV_64F).var()
        val_list.append(val)

    # find the index of max val
    index = max(range(len(list)), key=list.__getitem__)
    return index
    
