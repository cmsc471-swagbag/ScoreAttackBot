import win32api, win32con
import actionFunctions

#An Example GameAI with sample values
#All Values should be replaced and defined for a real game

"""
All coordinates assume a screen resolution of 1280x1024, and Chrome 
maximized with the Bookmarks Toolbar enabled.
Down key has been hit 4 times to center play area in browser.
"""
x_pad = 156
y_pad = 100
x_size = 800
y_size = 800

#The frequency at which gameIO should capture the screen for processing
#Represented in seconds
sampleRate = .1

#Failure state, defined as pixel location(x,y) and pixel color
#In this example, if pixel at 908, 400 has an r value of 65, a g value of 100, and a b value of 137
failure = (345, 400, 65, 100, 137)

#A Tuple containing the bounds of our game
bounds = (x_pad, y_pad, x_pad+x_size, y_pad+y_size)

#performs a set of actions to start the game from the main menu
def start():
    actionFunctions.leftClick()

#Performs a set of functions to reset the game from a failure state
#Should be called from GameIO when gameIO detects a failure 
def reset():
    actionFunctions.leftClick()

#Determines and performs action should take given input image
#Not doing anything should always be an option!
def chooseAction(image):
    actionFunctions.doNothing()
    




