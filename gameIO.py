#gameIO recieves input from the screen, passes it to gameAI and performs the action gameAI returns
#gameIO will never change except for line 4, but each game that the AI can play needs a gameAI file

import win32api, win32con
import pyscreenshot as ImageGrab
import os
import time
import exampleAI as gameAI #Replace 'exampleAI' with whatever file has the AI for the game you want to play 
 
def main():
    gameAI.start();
    while True:
        im = ImageGrab.grab(gameAI.bounds)  #get current screen
        if (im.getpixel((gameAI.failure[0], gameAI.failure[1])) == (gameAI.failure[2], gameAI.failure[3], gameAI.failure[4])): #is the pixel at the failure indicator the color that indicates failure?
            gameAI.reset()
        else:
            gameAI.chooseAction(im)

        time.sleep(gameAI.sampleRate)
        print("hi");
        
 
if __name__ == '__main__':
    main()
