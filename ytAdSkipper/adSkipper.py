# Created By Siddharth...

from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con


# Click Func 
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1) #This pauses the script for 0.1 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

# Skip func 
def skip_ad():
    while keyboard.is_pressed('Esc')==False:
        skip_button = pyautogui.locateCenterOnScreen("skipads.png",confidence=0.80)
        if skip_button!=None:
            print("ad Found!")
            x,y = skip_button
            print(x,y)
            click(x,y)
            sleep(0.5)
        # else:
            # print(time.gmtime())
            

skip_ad()

