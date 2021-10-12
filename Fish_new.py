import time
import cv2
import numpy as np
import imutils
from mss import mss
from mss import tools
import pyautogui
from datetime import datetime
import pydirectinput

# Test

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
    time.sleep(1.9)
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

        print("hook val: " + str(maxVal))
        if maxVal > 0.52:
            print("Waiting for Nibble: Hooked Fish!")
            timestamp(maxVal)
            pyautogui.mouseDown()
            pyautogui.mouseUp()
            return 1

        result = cv2.matchTemplate(edged, missed_template, cv2.TM_CCOEFF_NORMED)
        (_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)
        
        print("missed hook val: " + str(maxVal))
        if maxVal > 0.70:
            print("Waiting for Nibble: Missed Hook!")
            timestamp(maxVal)
            return 2
        
        result = cv2.matchTemplate(edged, wrong_template, cv2.TM_CCOEFF_NORMED)
        (_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)
        if maxVal > 0.80:
            print("Waiting for Nibble: Wrong State")
            timestamp(maxVal)
            return 3

def init_reel():
    print("Initial Reel To Bypass Hanging Fish Icon")
    for i in range(0,6):   
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

        # output = "test.png"
        # tools.to_png(img.rgb, img.size, output=output)
        # print(output)

        img = np.array(img)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        edged = cv2.Canny(gray, 50, 200)

        result = cv2.matchTemplate(edged, caught_template, cv2.TM_CCOEFF_NORMED)
        (_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)

        print("Reeling in Fish: missed caught val: " + str(maxVal))

        if maxVal > 0.65:
            print("Reeling in Fish: Caught Fishy!")
            timestamp(maxVal)
            pyautogui.mouseDown()
            pyautogui.mouseUp()
            return 1

        result = cv2.matchTemplate(edged, broke_template, cv2.TM_CCOEFF_NORMED)
        (_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)

        print("Reeling in Fish: line broke val: " + str(maxVal))

        if maxVal > 0.31:
            print("Line Broke!")
            timestamp(maxVal)
            return 2

        result = cv2.matchTemplate(edged, wrong_template, cv2.TM_CCOEFF_NORMED)
        (_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)

        print("Reeling in Fish: wrong state val: " + str(maxVal))

        if maxVal > 0.8:
            print("Reeling in Fish: Wrong State")
            timestamp(maxVal)
            return 3

def west():
    with mss() as sct:
        print("Locating hotspot based on yellow icon")
        timestamp("n/a")
        time.sleep(1)
        pyautogui.press('Escape')
        time.sleep(1)
        pyautogui.moveTo(510,418)
        time.sleep(1)
        pydirectinput.move(0,0)
        time.sleep(1)
        pyautogui.press('Escape')
        time.sleep(1)
        i = 0
        while(1):
            
            img = sct.grab(compass)
            # output = "test.png"
            # tools.to_png(img.rgb, img.size, output=output)
            # print(output)

            img = np.array(img)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            edged = cv2.Canny(gray, 50, 200)

            result = cv2.matchTemplate(edged, west_template, cv2.TM_CCOEFF_NORMED)
            (_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)
            print("West Threshold: " + str(maxVal))
            if maxVal > 0.65:
                print("West Found")
                timestamp(maxVal)
                break
            else:
                pydirectinput.move(1,0)
                i += 1

            if i > 500:
                # pyautogui.press('Escape')
                # time.sleep(1)
                pyautogui.moveTo(510,418)
                time.sleep(1)
                pydirectinput.move(0,0)
                time.sleep(1)
                pyautogui.press('Escape')
                time.sleep(1)
                i = 0

def repair():
    print("Repairing fishing rod.")
    timestamp("n/a")
    time.sleep(2)
    pyautogui.press('tab')
    pyautogui.moveTo(460, 580)
    time.sleep(2)
    pyautogui.keyDown('r')
    pyautogui.mouseDown()
    time.sleep(2)
    pyautogui.mouseUp()
    time.sleep(2)
    pyautogui.keyUp('r')
    pyautogui.press('e')
    time.sleep(2)
    pyautogui.press('Escape')
    time.sleep(2)
    pyautogui.press('F3')

def reset_rod():
    print("Resetting Fishing Rod.")
    timestamp("n/a")
    time.sleep(2)
    pyautogui.press('F3')
    time.sleep(3)
    pyautogui.press('F3')
    time.sleep(3)


###################################### Main Code ##############################################################
template = img_template("Hook.png")
caught_template = img_template("Caught!.png")
broke_template = img_template("Line_Broke!.png")
missed_template = img_template("Missed_Hook!.png")
repair_template = img_template("Repair.png")
wrong_template = img_template("Wrong_State.png")
west_template = img_template("West4.png")

run_cnt = 0

start_time = time.time()
mon = {'top': 180, 'left': 90, 'width': 930, 'height': 480}
compass = {'top': 30, 'left': 500, 'width': 25, 'height': 50}

repair_cnt = fish_cnt = missed_cnt = broke_cnt = wrong_cnt = reel_cnt = 0 
time.sleep(2)
while True:
    repair_cnt += 1
    cast()
    while True:
        hook_state = hook()
        if(hook_state == 1):
            break
        elif(hook_state == 2):
            missed_cnt += 1
            print("Missed Count: " + str(missed_cnt))
            cast()
        elif(hook_state == 3):
            print("Wrong State!")
            cast()
        
    init_reel()
    while True:
        reel_state = reel()
        if(reel_state == 1):
            fish_cnt += 1
            print("Fishies Caught: " + str(fish_cnt))
            west()
            break
        elif(reel_state == 2):
            broke_cnt += 1
            print("Line Broken: " + str(broke_cnt))
            break
        elif(reel_state == 3):
            wrong_cnt += 1
            print("Wrong State: " + str(wrong_cnt))
            west()
            break
        if reel_cnt > 200:
            reset_rod()
            reel_cnt = 0
            break
        reel_cnt+=1
    if repair_cnt > 50:
        repair()
        repair_cnt = 0
        run_cnt += 1
    # if run_cnt > 5000:
    #     break