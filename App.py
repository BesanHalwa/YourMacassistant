"""
"""

import cv2
import glob
import requests


English = 'eng'

self.api_key = fdcfa151c288957
self.language = language
self.payload = {
    'isOverlayRequired': True,
    'apikey': self.api_key,
    'language': self
    }


# main screen, camera open
def main_screen():
    cap = cv2.VideoCapture(0)

    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()


        # Display the resulting frame
        cv2.imshow('frame',frame)

        # capture if 'c'
        if cv2.waitKey(1) & 0xFF == ord('c'):
            capture()

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

# capture the frames
def capture():
    cap = cv2.VideoCapture(0)

    for num in range(50):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Display the resulting frame
        cv2.imshow('frame',frame)

        file_name = "temp/" + str(num) + "capture.jpg"

        # Store frame by frames
        cv2.imwrite(file_name,frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

# Detect the blur, find most relevent frames
def ret_index()
    val_list = []

    for img in glob.iglob("temp/*.jpg"):

        image = cv2.imread(img)
        val = cv2.Laplacian(image, cv2.CV_64F).var()
        val_list.append(val)

    # find the index of max val
    index = max(range(len(list)), key=list.__getitem__)
    return index
