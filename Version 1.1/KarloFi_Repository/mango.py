print("K-Tech Application Development Company")
print("Kar-LoFi Main Program - Python")
print("Version 1.1")

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

def my_function(multicheck):
    if websiteopen == "true" and multicheck == "false":
        webbrowser.get('firefox').open("https://www.youtube.com/watch?v=5qap5aO4i9A", new=1, autoraise=True)

while True:
	if pir.motion_detected:
		print("Motion Detected!")
		websiteopen = "true"
		#GPIO.output(8, GPIO.HIGH)
		#time.sleep(0.5)
		multicheck = my_function(multicheck)
		mutlicheck = "true"
		sleep(60)
	else:
		print("No Motion")
		websiteopen = "false"
		if websiteopen == "false" : os.system("killall firefox-esr")
		multicheck = "false"
		#GPIO.output(8, GPIO.LOW)
		time.sleep(1) 
