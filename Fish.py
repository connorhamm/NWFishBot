import time
import cv2
import numpy as np
import imutils
from mss import mss
from mss import tools
import pyautogui
from datetime import datetime
import pydirectinput

#test
############### Fix this garbage ########################################
template = cv2.imread("Hook.png")
template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
template = cv2.Canny(template, 50, 200)

caught_template = cv2.imread("Caught!.png")
caught_template = cv2.cvtColor(caught_template, cv2.COLOR_BGR2GRAY)
caught_template = cv2.Canny(caught_template, 50, 200)

broke_template = cv2.imread("Line_Broke!.png")
broke_template = cv2.cvtColor(broke_template, cv2.COLOR_BGR2GRAY)
broke_template = cv2.Canny(broke_template, 50, 200)

missed_template = cv2.imread("Missed_Hook!.png")
missed_template = cv2.cvtColor(missed_template, cv2.COLOR_BGR2GRAY)
missed_template = cv2.Canny(missed_template, 50, 200)

repair_template = cv2.imread("Repair.png")
repair_template = cv2.cvtColor(repair_template, cv2.COLOR_BGR2GRAY)
repair_template = cv2.Canny(repair_template, 50, 200)

wrong_template = cv2.imread("Wrong_State.png")
wrong_template = cv2.cvtColor(wrong_template, cv2.COLOR_BGR2GRAY)
wrong_template = cv2.Canny(wrong_template, 50, 200)

west_template = cv2.imread("285.png")
west_template = cv2.cvtColor(west_template, cv2.COLOR_BGR2GRAY)
west_template = cv2.Canny(west_template, 50, 200)

start_time = time.time()
mon = {'top': 180, 'left': 90, 'width': 930, 'height': 480}
compass = {'top': 30, 'left': 450, 'width': 100, 'height': 50}

def img_template(file):
    template = cv2.imread(file)
    template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    template = cv2.Canny(template, 50, 200)
    return template

################ Finish This! ##########################
def match_template(file):
    return 0

def timestamp(maxVal):
    print("Timestamp: " + str(datetime.now()))
    print("Threshold: " + str(maxVal))
    print("--------------------------")

def take_picture(img):
    output = "test.png"
    tools.to_png(img.rgb, img.size, output=output)
    print(output)

def cast():
    time.sleep(2)
    pyautogui.mouseDown()
    pyautogui.mouseUp()
    time.sleep(0.5)
    

def hook():
    with mss() as sct:
        last_time = time.time()
        img = sct.grab(mon)
        img = np.array(img)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        edged = cv2.Canny(gray, 50, 200)

        result = cv2.matchTemplate(edged, template, cv2.TM_CCOEFF_NORMED)
        (_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)

        if maxVal > 0.55:
            print("Hooked Fish!")
            timestamp(maxVal)
            pyautogui.mouseDown()
            pyautogui.mouseUp()
            return 1

        result = cv2.matchTemplate(edged, missed_template, cv2.TM_CCOEFF_NORMED)
        (_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)

        if maxVal > 0.80:
            print("Missed Hook!")
            timestamp(maxVal)
            return 2

def init_reel():
    for i in range(0,4):   
        pyautogui.mouseDown()
        time.sleep(0.25)
        pyautogui.mouseUp()
        time.sleep(0.25)

def reel():
    with mss() as sct:
        pyautogui.mouseDown()
        time.sleep(0.3)
        pyautogui.mouseUp()
        time.sleep(0.2)

        img = sct.grab(mon)
        img = np.array(img)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        edged = cv2.Canny(gray, 50, 200)

        result = cv2.matchTemplate(edged, caught_template, cv2.TM_CCOEFF_NORMED)
        (_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)
        if maxVal > 0.65:
            print("Caught Fishy!")
            timestamp(maxVal)
            pyautogui.mouseDown()
            pyautogui.mouseUp()
            return 1

        result = cv2.matchTemplate(edged, broke_template, cv2.TM_CCOEFF_NORMED)
        (_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)

        if maxVal > 0.7:
            print("Line Broke!")
            timestamp(maxVal)
            return 2

        result = cv2.matchTemplate(edged, wrong_template, cv2.TM_CCOEFF_NORMED)
        (_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)

        if maxVal > 0.9:
            print("Wrong State")
            timestamp(maxVal)
            return 3

def west():
    with mss() as sct:
        print("Locating hotspot")
        timestamp("n/a")
        pyautogui.press('Escape')
        time.sleep(1)
        pyautogui.moveTo(600,380)
        time.sleep(1)
        pyautogui.press('Escape')
        time.sleep(1)

        while(1):
            #pydirectinput.move(1,0)
            img = sct.grab(compass)
            # take_picture(img)

            img = np.array(img)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            edged = cv2.Canny(gray, 50, 200)

            result = cv2.matchTemplate(edged, west_template, cv2.TM_CCOEFF_NORMED)
            (_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)
            print("Threshold: " + str(maxVal))
            if maxVal > 0.7:
                print("West Found")
                timestamp(maxVal)
                break

def repair():
    print("Repairing fishing rod.")
    timestamp("n/a")
    time.sleep(2)
    pyautogui.press('tab')
    pyautogui.moveTo(460, 580)
    time.sleep(1)
    pyautogui.keyDown('r')
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()
    time.sleep(1)
    pyautogui.keyUp('r')
    pyautogui.press('e')
    time.sleep(1)
    pyautogui.press('Escape')
    time.sleep(1)
    pyautogui.press('F3')

###################################### Main Code ##############################################################
# repair_cnt, fish_cnt, missed_cnt, broke_cnt, wrong_cnt = 0
# time.sleep(2)
# while True:
#     repair_cnt += 1
#     cast()
#     while True:
#         hook_state = hook()
#         if(hook_state == 1):
#             break
#         elif(hook_state == 2):
#             missed_cnt += 1
#             print("Missed Count: " + str(missed_cnt))
#             cast()
#     init_reel()
#     while True:
#         reel_state = reel()
#         if(reel_state == 1):
#             fish_cnt += 1
#             print("Fishies Caught: " + str(fish_cnt))
#             west()
#             break
#         elif(reel_state == 2):
#             broke_cnt += 1
#             print("Line Broken: " + str(broke_cnt))
#             break
#         elif(reel_state == 3):
#             wrong_cnt += 1
#             print("Wrong State: " + str(wrong_cnt))
#             west()
#             break
#     if repair_cnt > 5:
#         repair()
#         repair_cnt = 0


# time.sleep(2)
# west()