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

image = "../images/csgoAccept.png"
image2 = "../images/img.jpg"

#####################################################
######################  USAGE  ######################
#####################################################
'''
python queue-clicker.py

Description:
This will trigger your computer to look for a
  FaceIt accept queue button every 15 seconds.

KILL:
This script can only be killed manually using
  CTRL + C via the Command Prompt
'''

print("Running...\n***\nMake sure FaceIt is on the main monitor.\n***")

def clicking():
    # Init time_running variable
    time_running = 0

    # Loop checking for Queue Image
    while True:
        # Check if Queue Image has popped (appeared on users screen)
        pos = pyautogui.locateOnScreen(image, confidence=0.9)
        if not (pos):
          pos = pyautogui.locateOnScreen(image2, confidence=0.9)

        # If Queue Image is present, click it
        if (pos):
            center = pyautogui.center(pos)
            pyautogui.click(center)
            print("Queue Accepted! Please kill this script manually via the Command prompt which you ran it from...")

        print(f"Checking for {(time_running*15)/60} minutes...")
        time_running += 1

        # Sleep for 15 seconds
        time.sleep(15)

clicking()
