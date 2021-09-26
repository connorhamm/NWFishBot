"""
1. Issue with fishing animation when catching fish
- fish in open area
2. Add check for misses
"""

import pyautogui
import cv2 as cv
import numpy as np
import os
from time import time
from PIL import ImageGrab

###############################################################################
# Compare screenshot with target image
###############################################################################
os.chdir(os.path.dirname(os.path.abspath(__file__)))
loop_time = time()
while(1):
    # Cast line startup
    # time.sleep(3)
    # pyautogui.mouseDown()
    # pyautogui.mouseUp()

    while(1):
        # Take Screenshot
        screenshot = pyautogui.screenshot()
        cv_image = np.array(myScreenshot)
        #cv_image = cv.cvtColor(myScreenshot, cv.COLOR_RGB2BGR)

        # Compare Target image and actual
        target_img = cv.imread("Start.png", cv.IMREAD_COLOR)
        # picture_img = cv.imread("Picture.jpg", cv.IMREAD_COLOR)

        # result = cv.matchTemplate(cv_image, target_img, cv.TM_CCOEFF_NORMED)
        # min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

        print('FPS {}'.format(1 / (time() - loop_time)))
        loop_time = time()
        # print(max_val)

        # if max_val > 0.8:
        #
        #     print('Best match confidence: %s' % max_val)
        #     print("Match Found")
        #     time.sleep(0.6)
        #     pyautogui.mouseDown()
        #     pyautogui.mouseUp()
        #     time.sleep(2)
        #     break
        # else:
        #     print("...")

    # Catch fish!
    while(1):
        pyautogui.mouseDown()
        time.sleep(1.3)

        pyautogui.mouseUp()
        time.sleep(1)
        # Take Screenshot
        myScreenshot2 = pyautogui.screenshot()
        myScreenshot2.save(r'Finish_Picture.jpg')

        # Compare Target image and actual
        target2_img = cv.imread("Finish.png", cv.IMREAD_UNCHANGED)
        picture2_img = cv.imread("Finish_Picture.jpg", cv.IMREAD_UNCHANGED)

        result2 = cv.matchTemplate(picture2_img, target2_img, cv.TM_CCOEFF_NORMED)

        min2_val, max2_val, min2_loc, max2_loc = cv.minMaxLoc(result2)

        if max2_val > 0.8:
            print('Best match confidence: %s' % max2_val)
            print("Match Found")
            pyautogui.mouseDown()
            pyautogui.mouseUp()
            time.sleep(1)
            pyautogui.mouseDown()
            pyautogui.mouseUp()
            break
        else:
            print("...")
