import Adafruit_DHT
sensor = Adafruit_DHT.DHT22
print("after sensor")
pin = 6 #GPIO4
humidity, tempearture = Adafruit_DHT.read_retry(sensor, pin)
print("after read temperature")
if humidity is not None and temperature is not None:
    print('Temp={0:0.1f}*C Huminity={1:0.1f}%'.format(temperature,humidity))
else:
    print('Failed to get reading. Try Again!')
