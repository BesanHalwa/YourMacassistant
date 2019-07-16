import numpy as np
import cv2
import os

import cv2
def start():
    cap = cv2.VideoCapture(0)
    # Capture frame-by-frame
    ret, frame = cap.read()

    flag = True
    while(flag):


        # Display the resulting frame
        cv2.imshow('frame',frame)
        ret, frame = cap.read()

        cv2.rectangle(frame,(300,80),(1280-300,720-80),(0,255,0),3)

        # capture if 'c'
        if cv2.waitKey(1) & 0xFF == ord('c'):
            capture()
            flag = False

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
    return 0


def capture():
    cap = cv2.VideoCapture(0)
    key = cv2.waitKey(20)

    for num in range(5):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Display the resulting frame
        cv2.imshow('frame',frame)

        file_name = "temp/capture.jpg"
        file_name1 = "temp/captureCropped.jpg"

        # Store frame by frames
        cv2.imwrite(file_name,frame)
        cropped_frame = frame[80:720-80, 300:1280-300]
        cv2.imwrite(file_name1,cropped_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
    return 0
