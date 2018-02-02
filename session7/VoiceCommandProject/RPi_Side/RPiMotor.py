import zmq
import RPi.GPIO as GPIO
import threading
import time

direction = 1
enable = 0
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
    GPIO.output(enablePin, False)
    CW_Rotate()
    while(1):
        if(direction == 1):
            CW_Rotate()
        elif(direction == 0)::
            CCW_Rotate()
        if(enable == 1):
            GPIO.output(enablePin, True)
        elif(enable == 0)
            GPIO.output(enablePin, False)
        time.sleep(0.01)

if __name__ == "__main__":
    t = threading.Thread(target=MotorAction)
    t.start()

    ctx = zmq.Context.instance()
    subscriber = ctx.socket(zmq.SUB)

    service_sensor_sub = "tcp://192.168.43.87:9999"

    subscriber.connect(service_sensor_sub)

    subscriber.set_string(zmq.SUBSCRIBE, unicode("start"))
    subscriber.set_string(zmq.SUBSCRIBE, unicode("stop"))
    subscriber.set_string(zmq.SUBSCRIBE, unicode("clockwise"))
    subscriber.set_string(zmq.SUBSCRIBE, unicode("counter clockwise"))

    while(1):
        buf = subscriber.recv_string()
        if(buf):
            if(buf == "clockwise"):
                direction = 1
            elif(buf == "counter clockwise"):
                direction = 0
            elif(buf == "start")
                enable = 1
            elif(buf == "stop")
                enable = 0
            print(buf)
