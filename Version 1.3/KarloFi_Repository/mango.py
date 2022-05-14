print("K-Tech Application Development Company")
print("Kar-LoFi Main Program - Python")
print("Version 1.3")

print("Importing Statements")
from gpiozero import MotionSensor
from subprocess import call
import RPi.GPIO as GPIO
import time
from time import sleep
from sys import exit
import webbrowser
import os

print("Detecting Hardware Alterations")
pir = MotionSensor(4)
GPIO.setmode(GPIO.BCM)

print("Integrating Code")
websiteopen = "false"
doubleup = "false"
counterDelay = 0

def my_function(multicheck, doubleup):
    if multicheck == "true" and doubleup == "false":
        webbrowser.get('firefox').open("https://www.youtube.com/watch?v=5qap5aO4i9A", new=1, autoraise=True)
        return "true"

def my_functionTwo(websiteopen):
    if websiteopen == "false": os.system("killall firefox-esr")

while True:
    if pir.motion_detected:
        print("Motion Detected")
        counterDelay = 0
        print("Resetted CounterDelay")
        print(counterDelay)
        websiteopen = "true"
        doubleup = my_function(websiteopen, doubleup)
        websiteopen = "false"
        time.sleep(1)
    else:
        print("No Motion")
        counterDelay = counterDelay + 1
        time.sleep(1)
        if counterDelay == 50:
            print("Resetted CounterDelay")
            doubleup = "false"
            my_functionTwo("false")
            counterDelay = 0
