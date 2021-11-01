"""
To Do:
1. Test program at home and optimize, use same location.
"""

import time
import pyautogui
import pydirectinput
from functions import *

class nwfish_bot:
    def __init__(self):
        self.template = img_template("./Images/Hook.png")
        self.caught_template = img_template("./Images/Caught!.png")
        self.broke_template = img_template("./Images/Line_Broke!.png")
        self.missed_template = img_template("./Images/Missed_Hook!.png")
        self.repair_template = img_template("./Images/Repair.png")
        self.wrong_template = img_template("./Images/Wrong_State.png")
        self.hotspot_template = img_template("./Images/hotspot.png")

        self.start_time = time.time()
        self.mon = {'top': 180, 'left': 90, 'width': 930, 'height': 480}
        self.compass = {'top': 30, 'left': 500, 'width': 25, 'height': 50}

        self.repair_cnt = 0
        self.fish_cnt = 0
        self.missed_cnt = 0
        self.broke_cnt = 0
        self.wrong_cnt = 0
        self.reel_cnt = 0 
        self.run_cnt = 0

        time.sleep(2)

        self.cast()

    def cast(self):
        print("State: Cast")
        time.sleep(2)
        pyautogui.mouseDown()
        time.sleep(1.9)
        pyautogui.mouseUp()
        time.sleep(0.5)
        
        self.fishing()

    def fishing(self):
        while(1):
            print("State: Fishing")
            edged_img = take_image(self.mon,True, "Fishing")
            hooked, _ = matchTemplate(self.template, edged_img, 0.52)
            missed_hook, _ = matchTemplate(self.missed_template, edged_img, 0.7)
            wrong, _ = matchTemplate(self.wrong_template, edged_img, 0.8)
            if hooked == True:
                print("Event: Hooked Fish!")
                pyautogui.mouseDown()
                pyautogui.mouseUp()
                self.init_reel()
            elif missed_hook == True:
                print("Event: Missed Hook!")
                break
            elif wrong == True:
                print("Event: Wrong State Detected!")
                break
        self.cast()
        
    def init_reel(self):
        print("State: Initial Reel")
        take_image(self.mon, True, "Initial_Reel")
        for i in range(0,6):   
            pyautogui.mouseDown()
            time.sleep(0.25)
            pyautogui.mouseUp()
            time.sleep(0.25)
        self.reel()

    def reel(self):
        print("State: Reel")
        while(1):
            pyautogui.mouseDown()
            time.sleep(0.3)
            pyautogui.mouseUp()
            time.sleep(0.2)        
            
            edged_img = take_image(self.mon,True, "Reel")
            caught, _ = matchTemplate(self.caught_template, edged_img, 0.65)
            broke, _ = matchTemplate(self.broke_template, edged_img, 0.31)
            wrong, _ = matchTemplate(self.wrong_template, edged_img, 0.8)

            if caught == True:
                print("Event: Caught Fish")
                self.fish_cnt += 1
                pyautogui.mouseDown()
                pyautogui.mouseUp()
                break
            elif broke == True:
                print("Event: Line Broke")
                self.broke_cnt += 1
                break
            elif wrong == True:
                print("Event: Wrong State Detected")
                self.wrong_cnt += 1
                break
        self.hotspot()

    def hotspot(self):
        print("State: Locate Hotspot")
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
            edged_img = take_image(self.compass,True, "Hotspot")
            hotspot, _ = matchTemplate(self.hotspot_template, edged_img, 0.65)

            if hotspot == True:
                print("Event: Hotspot Found")
            else:
                pydirectinput.move(1,0)
                i += 1

            if i > 500:
                pyautogui.moveTo(510,418)
                time.sleep(1)
                pydirectinput.move(0,0)
                time.sleep(1)
                pyautogui.press('Escape')
                time.sleep(1)
                i = 0
        self.reset_rod()
        self.repair()

    def reset_rod(self):
        print("Resetting Fishing Rod.")
        timestamp("n/a")
        time.sleep(2)
        pyautogui.press('F3')
        time.sleep(3)
        pyautogui.press('F3')
        time.sleep(3)

    def repair(self):
        print("State: Repair")
        take_image(self.compass,True, "Repair")
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
        time.sleep(1)

###################################### Main Code ##############################################################
print("Welcome to SlyTurtle's New World FIshing Bot")
nwfish_bot()