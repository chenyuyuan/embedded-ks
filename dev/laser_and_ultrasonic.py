#!/usr/bin/env python
#####################################################
#
#	DO NOT WATCH THE LASER DIRECTELY IN THE EYE!
#
#####################################################
import RPi.GPIO as GPIO
import time

LedPin = 35
TRIG = 38
ECHO = 40

def main():
	GPIO.setmode(GPIO.BOARD)       
	GPIO.setup(TRIG, GPIO.OUT)
	GPIO.setup(ECHO, GPIO.IN)
	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
	GPIO.setup(LedPin, GPIO.OUT)   # Set LedPin's mode is output
	GPIO.output(LedPin, GPIO.HIGH) # Set LedPin high(+3.3V) to off led

	print('...Laser on')
	GPIO.output(LedPin, GPIO.LOW)  # led on

	GPIO.output(TRIG, 0)
	time.sleep(0.000002)
	GPIO.output(TRIG, 1)
	time.sleep(0.00001)
	GPIO.output(TRIG, 0)

	while GPIO.input(ECHO) == 0:
		a = 0
	time1 = time.time()
	while GPIO.input(ECHO) == 1:
		a = 1
	time2 = time.time()
	during = time2 - time1
	dis = int(during * 340 / 2 * 100)
	print(str(dis)+'cm')
	time.sleep(0.5)

	print('...Laser off')
	GPIO.output(LedPin, GPIO.HIGH) # led off
	time.sleep(0.5)

	GPIO.output(LedPin, GPIO.HIGH)

	GPIO.cleanup()


if __name__ == '__main__':     # Program start from here
	try:
		main()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()

