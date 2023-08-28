import pyautogui
import time

#####################################################
##################  PREREQUISITES  ##################
#####################################################
# pip install pyautogui
# pip install opencv-python
# time library is part of python

# Add an image to the images folder and be sure to
#   change the image variable so it matches the name
#   of you image (i.e., img.jpg | button.png | etc.)
#####################################################
#####################################################

#####################################################
######################  USAGE  ######################
#####################################################
# Call the script using:
# python queue-clicker.py 
# This will trigger your computer to look for an 
#   accept queue button every 15 seconds. 
# KILL: This script will be killed once it accepts..
#####################################################
#####################################################

image = "images/img.jpg"

print("Waiting to accept queue...")

def clicking():
    while True:
        pos = pyautogui.locateOnScreen(image, confidence=0.9)
        print(pos)
        if (pos):
            center = pyautogui.center(pos)
            pyautogui.click(center)

        print("Checking..")
        
        time.sleep(15)
        
clicking()