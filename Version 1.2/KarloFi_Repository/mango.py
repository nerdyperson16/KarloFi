print("K-Tech Application Development Company")
print("Kar-LoFi Main Program - Python")
print("Version 1.2")

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
#GPIO.setup(8, GPIO.OUT)

print("Integrating Code")
websiteopen = "false"
multicheck = "false"
counterDelay = 0

def my_function(multicheck):
    if websiteopen == "true" and multicheck == "false":
    	webbrowser.get('firefox').open("https://www.youtube.com/watch?v=5qap5aO4i9A", new=1, autoraise=True)
		mutlicheck = "false"
		websiteopen = "false"

def my_functionTwo(websiteopen):
	if websiteopen == "false" : os.system("killall firefox-esr")

while True:
	if pir.motion_detected:
		print("Motion Detected!")
		websiteopen = "true"
		#GPIO.output(8, GPIO.HIGH)
		#time.sleep(0.5)
		multicheck = my_function(multicheck)
		mutlicheck = "true"
	else:
		print("No Motion")
		counterDelay = counterDelay + 1
		if counterDelay = 50:
			websiteopen = "false"
			my_functionTwo("false")
		multicheck = "false"
		#GPIO.output(8, GPIO.LOW)
		time.sleep(1)