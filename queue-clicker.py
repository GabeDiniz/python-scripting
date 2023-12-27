import pyautogui
import time

#####################################################
##################  PREREQUISITES  ##################
#####################################################
'''
pip install pyautogui
time library is part of python

Add an image to the images folder and be sure to
  change the image variable (line 16) so it matches 
  the name of your image.
  (i.e., img.jpg | button.png | etc.) 
'''

image = "images/img.jpg"

#####################################################
######################  USAGE  ######################
#####################################################
'''
python queue-clicker.py 

Description:
This will trigger your computer to look for an 
  accept queue button every 15 seconds.

KILL: 
This script can only be killed manually using 
  CTRL + C via the Command Prompt
'''

print("Running...\n***\nPlease ensure your game is tabbed in on your main monitor.\n***")

def clicking():
    while True:
        pos = pyautogui.locateOnScreen(image, confidence=0.9)
        if (pos):
            center = pyautogui.center(pos)
            pyautogui.click(center)

        print("Checking..")
        
        time.sleep(15)
        
clicking()