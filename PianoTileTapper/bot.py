# Created By Siddharth...
from pyautogui import *
import pyautogui 
import time
import keyboard
import random
import win32api, win32con
import sys

# Link of piano Website - https://www.agame.com/game/magic-piano-tiles
# Dont Forget To :
# 1. Switch top full screen
# 2. First Pause the game
# 3. Run The Program 
# 4. Start The program and Unpause the game


# Click Func 
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1) #This pauses the script for 0.1 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

# Tiles x and y locations
# X:  720 Y:  1000 RGB: (  0,   0,   0)
# X:  886 Y:  1000 RGB: ( 82,  86, 117)
# X: 1040 Y:  1000 RGB: ( 81,  85, 116)
# X: 1206 Y:  1000 RGB: ( 87,  87, 117)
y = 400
def piano_tile_tapper():
    pyautogui.alert(text='Start', title='', button='OK')
    while keyboard.is_pressed('Esc')==False:
        if pyautogui.pixel(746,y)[0] == 0 :
            click(720,y)
            print("Pressed")
        if pyautogui.pixel(886,y)[0] == 0 :
            click(886,y)
            print("Pressed")
        if pyautogui.pixel(1193,y)[0] == 0 :
            click(1193,y)
            print("Pressed")
        if pyautogui.pixel(1030,y)[0] == 0 :
            click(1039,y)
            print("Pressed")
       
        


piano_tile_tapper()