import sys
import time
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

mode=GPIO.getmode()

motor_pins=(11,12,13,15) #Yellow Red Green Gray


ledPin = 36
buttonPin = 38


GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#Motor section
GPIO.setup(motor_pins, GPIO.OUT)
step_number=1000
inputdelay=0.001
steps = int(step_number)

GPIO.output(motor_pins, (GPIO.LOW,GPIO.LOW,GPIO.LOW,GPIO.LOW))

try:
    while(True):
          buttonState = GPIO.input(buttonPin)
          if buttonState == False:
                GPIO.output(ledPin, GPIO.HIGH)
                GPIO.output(motor_pins, (GPIO.HIGH,GPIO.LOW,GPIO.HIGH,GPIO.LOW))
                sleep(inputdelay)
                GPIO.output(motor_pins, (GPIO.LOW,GPIO.HIGH,GPIO.HIGH,GPIO.LOW))
                sleep(inputdelay)
                GPIO.output(motor_pins, (GPIO.LOW,GPIO.HIGH,GPIO.LOW,GPIO.HIGH))
                sleep(inputdelay)
                GPIO.output(motor_pins, (GPIO.HIGH,GPIO.LOW,GPIO.LOW,GPIO.HIGH))
                sleep(inputdelay)
                #sleep(10000)
          else:
                GPIO.output(ledPin, GPIO.LOW)
      
except KeyboardInterrupt:
    GPIO.cleanup()
