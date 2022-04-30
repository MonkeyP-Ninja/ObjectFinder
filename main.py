import cv2 as cv
import numpy as np
import time



pTime = 0.0
cTime = 0.0
cap = cv.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

cap.set(1,60)

if (cap.isOpened() == False):
    print("Error opening video  file")

# Read until video is completed
while (cap.isOpened()):

    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret == True:

        # Display the resulting frame

        cTime = time.time()
        fps = int(1 / (cTime - pTime))
        pTime = cTime
        cv.putText(frame, str(fps), (10, 70), cv.FONT_HERSHEY_COMPLEX_SMALL, 5, (255, 0, 255), 3)
        cv.imshow('Frame', frame)

        # Press Q on keyboard to  exit
        if cv.waitKey(25) & 0xFF == ord('q'):
            break

    # Break the loop
    else:
        break





def find_minion():
    print('ff')
























