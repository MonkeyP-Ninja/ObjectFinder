import pyautogui
import cv2
import numpy as np


img = pyautogui.screenshot(region=(0, 0, 1920, 1080))
image = np.array(img)
# Convert RGB to BGR


dim=(1280,720)
resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
cv2.cvtColor(image,cv2.COLOR_BGR2RGB)




cv2.imshow('tes', resized)
cv2.waitKey(0)

