import numpy as np
import cv2

def main():
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

if __name__ == '__main__':
    main()
