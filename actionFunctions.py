#This File contains sets of win32api calls for common functions needed in all games
#Examples being a left click, a hold down for a set duration
#Not all Action functions need to be defined here

#Testing commit functionality


import win32api, win32con
import time

def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def leftHold(time):
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(time)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    
def doNothing():
    return
