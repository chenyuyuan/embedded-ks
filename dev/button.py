#!/usr/bin/env python
import RPi.GPIO as GPIO

BtnPin = 29


def setup():
	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
	GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Set BtnPin's mode is input, and pull up to high level(3.3V)
	GPIO.add_event_detect(BtnPin, GPIO.BOTH, callback=detect, bouncetime=200)

def Print(x):
	if x == 0:
		print '    ***********************'
		print '    *   Button Pressed!   *'
		print '    ***********************'
        elif x == 1:
                print 'it 1'
        
def detect(chn):
	Print(GPIO.input(BtnPin))

def loop():
	while True:
		pass

def destroy():
	GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()

