import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

#pin number for each light
RED = 17
GREEN = 23
AMBER = 6

#initialize the states
GPIO.setup(RED, GPIO.OUT)
GPIO.output(RED,GPIO.LOW)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.output(GREEN,GPIO.LOW)
GPIO.setup(AMBER, GPIO.OUT)
GPIO.output(AMBER,GPIO.LOW)

#functions
def red(howlong):
        setLight(RED, howlong)

def green(howlong):
        setLight(GREEN, howlong)

def amber(howmanytimes, howlong):
        for i in range(howmanytimes):
                setLight(AMBER, howlong)
                time.sleep(howlong)

def setLight(light, howlong):
        GPIO.output(light,GPIO.HIGH)
        time.sleep(howlong)
        GPIO.output(light,GPIO.LOW)
        
def traffic():
        while(True):
                red(3)
                green(2)
                amber(3, 1)
            
#main function
traffic()