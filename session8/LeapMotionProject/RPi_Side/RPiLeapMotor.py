import zmq
import RPi.GPIO as GPIO
import threading

cw = 1
ccw = 2

direction = cw
speed = 0
enablePin = 18
in1Pin = 23
in2Pin = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1Pin, GPIO.OUT)
GPIO.setup(in2Pin, GPIO.OUT)
GPIO.setup(enablePin, GPIO.OUT)

def CW_Rotate():
    GPIO.output(in1Pin, False)
    GPIO.output(in2Pin, True)

def CCW_Rotate():
    GPIO.output(in1Pin, True)
    GPIO.output(in2Pin, False)

def MotorAction():
    pwm = GPIO.PWM(enablePin, 500)
    pwm.start(0)
    CW_Rotate()
    while(1):
        if(direction == cw):
            CW_Rotate()
        else:
            CCW_Rotate()
        pwm.ChangeDutyCycle(speed)

if __name__ == "__main__":
    t = threading.Thread(target=MotorAction)
    t.start()

    ctx = zmq.Context.instance()
    subscriber = ctx.socket(zmq.SUB)

    service_sensor_sub = "tcp://192.168.43.87:9999"

    subscriber.connect(service_sensor_sub)

    subscriber.set_string(zmq.SUBSCRIBE, unicode("CW:"))
    subscriber.set_string(zmq.SUBSCRIBE, unicode("CC:"))

    while(1):
        buf = subscriber.recv_string()
        if(buf):
            if(buf[0:3] == "CW:"):
                direction = cw
            else:
                direction = ccw

            speed = int(buf[3:5])
            print(buf)
