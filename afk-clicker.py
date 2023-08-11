import pyautogui
import time
import argparse

#####################################################
##################  PREREQUISITES  ##################
#####################################################
# pip install pyautogui
# time and argparse library are part of python
#####################################################
#####################################################

#####################################################
######################  USAGE  ######################
#####################################################
# Call the script using:
# python afk-clicker.py -t <time in minutes>
# This will trigger your computer to left-click 
#       every 30 seconds..
# WARNING: This script does not care what application 
#       you are in.. it will left click regardless
# KILL: This script can only be killed manually..
#####################################################
#####################################################

## Argument Parser
parser = argparse.ArgumentParser()
parser.add_argument("-t", "--time", type=int)

## Arguments
args = parser.parse_args()

def clicker():
    pyautogui.click()

print(f"Running for {args.time} minutes")

def clicking():
    time.sleep(10)
    x = 1
    # Script will auto-click every 30 seconds...
    while x < (args.time * 2):
        print(str(args.time - (x / 2)) + " minutes left")
        clicker()
        time.sleep(30)
        x = x + 1
        
clicking()