
import RPi.GPIO as GPIO
import time
 
def delay(i):
	while i:
		i -= 1
 
def init_dht11(dht11_pin):
	GPIO.setup(dht11_pin, GPIO.OUT)
	GPIO.output(dht11_pin, 1)
 
def get_dht11(dht11_pin):
	buff=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
 
	GPIO.output(dht11_pin,0)
	time.sleep(0.02)
 
	GPIO.output(dht11_pin,1)
 
	GPIO.setup(dht11_pin,GPIO.IN)
 
	while not GPIO.input(dht11_pin):
		pass
  
	while GPIO.input(dht11_pin):
		pass
 
	i=40
 
	while i:
		start=time.time()*1000000
		i-=1
		#print(i)
		#print(buff)
		while not GPIO.input(dht11_pin):
			pass
		while GPIO.input(dht11_pin):
			pass
		buff[i]=time.time()*1000000-start
                #print("after second circle")
 
	GPIO.setup(dht11_pin,GPIO.OUT)
	GPIO.output(dht11_pin,1)
 
 
	for i in range(len(buff)):
		if buff[i]>100:
			buff[i]=1
		else:
			buff[i]=0
 
 
	i=40
	hum_int=0
	while i>32:
		i-=1
		hum_int<<=1
		hum_int+=buff[i]
	# print "hum - ",hum_int
 
	tmp_int=0
	i=24
	while i>16:
		i-=1
		tmp_int<<=1
		tmp_int+=buff[i]
	# print "tmp - ",tmp_int
	return [hum_int,tmp_int]

if __name__ == "__main__":
        GPIO.setmode(GPIO.BOARD)
        init_dht11(11)
        print (get_dht11(11))
        GPIO.cleanup()
