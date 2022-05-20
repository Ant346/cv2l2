import keyboard
import mss
import cv2
import numpy as np
from time import time, sleep
import pyautogui


wheat_img=cv2.imread('orc.png',cv2.IMREAD_UNCHANGED)

im1 = pyautogui.screenshot()
im1.save('my_screenshot.png')
farm_img=cv2.imread('my_screenshot.png',cv2.IMREAD_UNCHANGED)

result=cv2.matchTemplate(farm_img,wheat_img,cv2.TM_CCOEFF_NORMED)
min_val,max_val,min_loc,max_loc=cv2.minMaxLoc(result)
w=wheat_img.shape[1]
h=wheat_img.shape[0]
cv2.rectangle(farm_img, max_loc, (max_loc[0]+w, max_loc[1]+h), (0,255,255), 2)
treshold=.60
yloc, xloc=np.where(result>=treshold)
print(len(xloc))

for (x,y) in zip(xloc,yloc):
    cv2.rectangle(farm_img, (x,y), (x+w, y+h), (0,255,255), 2)

cv2.imshow('Farm',farm_img)
cv2.waitKey()
cv2.destroyAllWindows()