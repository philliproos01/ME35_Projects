import sys
import time
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

mode=GPIO.getmode()

#knife motor pins
motor_pins=(11,12,13,15) #Yellow Red Green Gray
motor_pins2=(35,36,37,38) #Yellow Red Green Gray

#linear actuator motor
motor_pins3=(29,31,33,32)

#Motor section
GPIO.setup(motor_pins, GPIO.OUT)
GPIO.setup(motor_pins2, GPIO.OUT)
GPIO.setup(motor_pins3, GPIO.OUT)
step_number=1000
inputdelay=0.005
steps = int(step_number)

def linear_retract():
  for x in range(1227):
  #GPIO.output(motor_pins, (GPIO.LOW,GPIO.LOW,GPIO.LOW,GPIO.LOW))
  #GPIO.output(ledPin, GPIO.HIGH)
     GPIO.output(motor_pins3, (GPIO.HIGH,GPIO.LOW,GPIO.HIGH,GPIO.LOW))
     sleep(inputdelay)
     GPIO.output(motor_pins3, (GPIO.LOW,GPIO.HIGH,GPIO.HIGH,GPIO.LOW))
     sleep(inputdelay)
     GPIO.output(motor_pins3, (GPIO.LOW,GPIO.HIGH,GPIO.LOW,GPIO.HIGH))  
     sleep(inputdelay)
     GPIO.output(motor_pins3, (GPIO.HIGH,GPIO.LOW,GPIO.LOW,GPIO.HIGH))
  

def linear():
  for x in range(100):
	#GPIO.output(motor_pins, (GPIO.LOW,GPIO.LOW,GPIO.LOW,GPIO.LOW))
	#GPIO.output(ledPin, GPIO.HIGH)
    GPIO.output(motor_pins3, (GPIO.HIGH,GPIO.LOW,GPIO.LOW,GPIO.HIGH))
    sleep(inputdelay)
    GPIO.output(motor_pins3, (GPIO.LOW,GPIO.HIGH,GPIO.LOW,GPIO.HIGH))
    sleep(inputdelay)
    GPIO.output(motor_pins3, (GPIO.LOW,GPIO.HIGH,GPIO.HIGH,GPIO.LOW))
    sleep(inputdelay)
    GPIO.output(motor_pins3, (GPIO.HIGH,GPIO.LOW,GPIO.HIGH,GPIO.LOW))
    sleep(inputdelay)

def chop():
  for x in range(11):
  #GPIO.output(motor_pins, (GPIO.LOW,GPIO.LOW,GPIO.LOW,GPIO.LOW))
  #GPIO.output(ledPin, GPIO.HIGH)
  

    GPIO.output(motor_pins2, (GPIO.HIGH,GPIO.LOW,GPIO.HIGH,GPIO.LOW))
    GPIO.output(motor_pins, (GPIO.HIGH,GPIO.LOW,GPIO.LOW,GPIO.HIGH))
    sleep(inputdelay)
    GPIO.output(motor_pins, (GPIO.LOW,GPIO.HIGH,GPIO.LOW,GPIO.HIGH))
    GPIO.output(motor_pins2, (GPIO.LOW,GPIO.HIGH,GPIO.HIGH,GPIO.LOW))
    sleep(inputdelay)
    GPIO.output(motor_pins, (GPIO.LOW,GPIO.HIGH,GPIO.HIGH,GPIO.LOW))
    GPIO.output(motor_pins2, (GPIO.LOW,GPIO.HIGH,GPIO.LOW,GPIO.HIGH))
    sleep(inputdelay)
    GPIO.output(motor_pins, (GPIO.HIGH,GPIO.LOW,GPIO.HIGH,GPIO.LOW))
    GPIO.output(motor_pins2, (GPIO.HIGH,GPIO.LOW,GPIO.LOW,GPIO.HIGH))
    sleep(inputdelay)  
  
  for x in range(20):
  #GPIO.output(motor_pins, (GPIO.LOW,GPIO.LOW,GPIO.LOW,GPIO.LOW))
  #GPIO.output(ledPin, GPIO.HIGH)
  

    GPIO.output(motor_pins, (GPIO.HIGH,GPIO.LOW,GPIO.HIGH,GPIO.LOW))
    GPIO.output(motor_pins2, (GPIO.HIGH,GPIO.LOW,GPIO.LOW,GPIO.HIGH))
    sleep(inputdelay)
    GPIO.output(motor_pins2, (GPIO.LOW,GPIO.HIGH,GPIO.LOW,GPIO.HIGH))
    GPIO.output(motor_pins, (GPIO.LOW,GPIO.HIGH,GPIO.HIGH,GPIO.LOW))
    sleep(inputdelay)
    GPIO.output(motor_pins2, (GPIO.LOW,GPIO.HIGH,GPIO.HIGH,GPIO.LOW))
    GPIO.output(motor_pins, (GPIO.LOW,GPIO.HIGH,GPIO.LOW,GPIO.HIGH))
    sleep(inputdelay)
    GPIO.output(motor_pins2, (GPIO.HIGH,GPIO.LOW,GPIO.HIGH,GPIO.LOW))
    GPIO.output(motor_pins, (GPIO.HIGH,GPIO.LOW,GPIO.LOW,GPIO.HIGH))
    sleep(inputdelay)
    #sleep(10000)
#sleep(10000)
def process():
    for x in range(12):
        chop();
        chop();
        chop();
        linear();

    linear_retract();
   
process();
 #retract after
