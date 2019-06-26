from flask import Flask
from flask import render_template,request
import RPi.GPIO as GPIO
import time
import sqlite3
import json

Rpin = 29
Gpin = 31
Bpin = 33

Buzzer = 32

CL = [0, 131, 147, 165, 175, 196, 211, 248]		# Frequency of Low C notes
CM = [0, 262, 294, 330, 350, 393, 441, 495]		# Frequency of Middle C notes
CH = [0, 525, 589, 661, 700, 786, 882, 990]		# Frequency of High C notes

app = Flask(__name__)

@app.route('/')
def home():
    conn = sqlite3.connect('dev.db')
    curs = conn.cursor()
    temp_data=[]
    for row in curs.execute("SELECT * FROM temps ORDER BY time DESC"):
        temp_data.append(row)
    conn.commit()
    conn.close()

    conn = sqlite3.connect('rgb.db')
    curs = conn.cursor()
    rgb_data=[]
    for row in curs.execute("SELECT * FROM temps ORDER BY id DESC"):
        rgb_data.append(row)
    conn.commit()
    conn.close()

    
    return render_template("control.html",listtemp=temp_data,listrgb=rgb_data)

@app.route('/he')
def hello_world():
    return 'Hello World!'

@app.route('/gettemp',methods=['GET','POST'])
def temperature():
    file = open('/sys/bus/w1/devices/28-01187a999cff/w1_slave')
    text = file.read()
    temp=float(text[-6:-1])/1000
    print(temp)
    file.close()
    
    conn = sqlite3.connect('dev.db')
    curs = conn.cursor()
    curs.execute("INSERT INTO temps(temperature) VALUES((?))",(temp,))
    conn.commit()
    conn.close()
    
    return str(temp)

@app.route('/listtemp',methods=['GET','POST'])
def listtemp():
    conn = sqlite3.connect('dev.db')
    curs = conn.cursor()
    data=[]
    for row in curs.execute("SELECT * FROM temps ORDER BY time DESC"):
        data.append(row)
    conn.commit()
    conn.close()
    return json.dumps({"data":data})

@app.route('/listrgb',methods=['GET','POST'])
def listrgb():
    conn = sqlite3.connect('rgb.db')
    curs = conn.cursor()
    data=[]
    for row in curs.execute("SELECT * FROM temps ORDER BY id DESC"):
        data.append(row)
    conn.commit()
    conn.close()
    return json.dumps({"data":data})


@app.route('/playsound',methods=['GET','POST'])
def play_sound():
    req = request.get_json()
    soundnumber = req['soundnumber']
    GPIO.setmode(GPIO.BOARD)		# Numbers GPIOs by physical location
    GPIO.setup(Buzzer, GPIO.OUT)	# Set pins' mode is output
    global Buzz						# Assign a global variable to replace GPIO.PWM 
    Buzz = GPIO.PWM(Buzzer, 440)	# 440 is initial frequency.
    Buzz.start(50)
    if soundnumber<=7:
        Buzz.ChangeFrequency(CL[soundnumber-0])	# Change the frequency along the song note
    elif soundnumber<=17:
        Buzz.ChangeFrequency(CM[soundnumber-10])
    elif soundnumber<=27:
        Buzz.ChangeFrequency(CH[soundnumber-20])
    time.sleep(0.5)
    Buzz.stop()					# Stop the buzzer
    GPIO.output(Buzzer, 1)		# Set Buzzer pin to High
    GPIO.cleanup()
    return "Hello World!"

@app.route('/rgb_led',methods=['GET','POST'])
def rgb_led():
    req = request.get_json()
    r_val = req['rvalue']
    g_val = req['gvalue']
    b_val = req['bvalue']

    conn = sqlite3.connect('rgb.db')
    curs = conn.cursor()
    curs.execute("INSERT INTO temps(r,g,b) VALUES((?),(?),(?))",(r_val,g_val,b_val,))
    conn.commit()
    conn.close()
    
    print("led start")
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Rpin, GPIO.OUT)   # Set pins' mode is output
    GPIO.output(Rpin, GPIO.HIGH) # Set pins to high(+3.3V)
    GPIO.setup(Gpin, GPIO.OUT)   # Set pins' mode is output
    GPIO.output(Gpin, GPIO.HIGH) # Set pins to high(+3.3V)
    GPIO.setup(Bpin, GPIO.OUT)   # Set pins' mode is output
    GPIO.output(Bpin, GPIO.HIGH) # Set pins to high(+3.3V)


    p_R = GPIO.PWM(Rpin, 2000)  # set Frequece to 2KHz
    p_G = GPIO.PWM(Gpin, 2000)
    p_B = GPIO.PWM(Bpin, 2000)

    p_R.start(100)
    p_G.start(100)
    p_B.start(100)

    r_val = float(r_val)/255.0*100
    g_val = float(g_val)/255.0*100
    b_val = float(b_val)/255.0*100

    print(str(r_val)+" "+str(g_val)+" "+str(b_val))

    p_R.ChangeDutyCycle(r_val)
    p_G.ChangeDutyCycle(g_val)
    p_B.ChangeDutyCycle(b_val)

    #grey_degree = ((r_val**2.2)*0.2126+(g_val**2.2)*0.7152+(b_val**2.2)*0.0722)**(1/2.2)

    time.sleep(3)

    p_R.stop()
    p_G.stop()
    p_B.stop()
    GPIO.output(Rpin, GPIO.HIGH)
    GPIO.output(Gpin, GPIO.HIGH)
    GPIO.output(Bpin, GPIO.HIGH)

    GPIO.cleanup()

    print("led end")
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
