import time
import cv2
import numpy as np
import imutils
from mss import mss
import pyautogui

template = cv2.imread("Hook.png")
template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
template = cv2.Canny(template, 50, 200)
(h, w) = template.shape[:2]

caught_template = cv2.imread("Caught!.png")
caught_template = cv2.cvtColor(caught_template, cv2.COLOR_BGR2GRAY)
caught_template = cv2.Canny(caught_template, 50, 200)
(h ,w) = caught_template.shape[:2]

broke_template = cv2.imread("Line_Broke!.png")
broke_template = cv2.cvtColor(broke_template, cv2.COLOR_BGR2GRAY)
broke_template = cv2.Canny(broke_template, 50, 200)
(h ,w) = broke_template.shape[:2]

missed_template = cv2.imread("Missed_Hook!.png")
missed_template = cv2.cvtColor(missed_template, cv2.COLOR_BGR2GRAY)
missed_template = cv2.Canny(missed_template, 50, 200)
(h ,w) = missed_template.shape[:2]

start_time = time.time()
mon = {'top': 180, 'left': 90, 'width': 930, 'height': 480}

while True:
    time.sleep(3)
    pyautogui.mouseDown()
    pyautogui.mouseUp()

    with mss() as sct:
        while True:
            last_time = time.time()
            img = sct.grab(mon)
            img = np.array(img)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            edged = cv2.Canny(gray, 50, 200)

            result = cv2.matchTemplate(edged, template, cv2.TM_CCOEFF_NORMED)
            (_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)

            #print('Best match confidence: %s' % maxVal)
            #print('The loop took: {0}'.format(time.time()-last_time))
            #cv2.imshow('test', np.array(img))
            # cv2.imshow('test', img)

            if maxVal > 0.50:
                print(maxVal)
                print("Hooked Fish!")
                pyautogui.mouseDown()
                pyautogui.mouseUp()
                break

            result = cv2.matchTemplate(edged, missed_template, cv2.TM_CCOEFF_NORMED)
            (_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)

            if maxVal > 0.80:
                print(maxVal)
                print("Missed Hook!")

        # initial reel
        print("Reeling in the fishies...")
        pyautogui.mouseDown()
        time.sleep(1)
        pyautogui.mouseUp()
        time.sleep(1)
        print("Reeling in the fishies...")
        pyautogui.mouseDown()
        time.sleep(1)
        pyautogui.mouseUp()
        time.sleep(1)

        while True:
            print("Reeling in the fishies...")
            pyautogui.mouseDown()
            time.sleep(1)
            pyautogui.mouseUp()
            time.sleep(1)

            img = sct.grab(mon)
            img = np.array(img)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            edged = cv2.Canny(gray, 50, 200)

            result = cv2.matchTemplate(edged, caught_template, cv2.TM_CCOEFF_NORMED)
            (_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)

            if maxVal > 0.75:
                print(maxVal)
                print("Caught Fishy!")
                pyautogui.mouseDown()
                pyautogui.mouseUp()
                break

            result = cv2.matchTemplate(edged, broke_template, cv2.TM_CCOEFF_NORMED)
            (_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)

            if maxVal > 0.7:
                print(maxVal)
                print("Line Broke!")
                break
