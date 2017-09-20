######################################################################
#       Web_Control.py
#
# This program control 3 LED and read button status with
# a web interface
######################################################################

from bottle import route, run
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
LedPins = [18, 23, 24]
LedStates = [0, 0, 0]
SwitchPin = 25

GPIO.setup(LedPins[0], GPIO.OUT)
GPIO.setup(LedPins[1], GPIO.OUT)
GPIO.setup(LedPins[2], GPIO.OUT)
GPIO.setup(SwitchPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def GetSwitchStatus():
    state = GPIO.input(SwitchPin)
    if state:
        return 'Up'
    else:
        return 'Down'

def HtmlForLed(led):
    l = str(led)
    result = " <input type='button' onClick='changed(" + l + ")' value='LED " + l + "'/>"
    return result

def UpdateLeds():
    for i, value in enumerate(LedStates):
        GPIO.output(LedPins[i], value)

@route('/')
@route('/<led>')
def index(led="n"):
    print(led)
    if led != "n":
        LedNum = int(led)
        LedStates[LedNum] = not LedStates[LedNum]
        UpdateLeds()
    response = "<script>"
    response += "function changed(led)"
    response += "{"
    response += "  window.location.href='/' + led"
    response += "}"
    response += "</script>"
    
    response += '<h1>GPIO Control</h1>'
    response += '<h2>Button=' + GetSwitchStatus() + '</h2>'
    response += '<h2>LEDs</h2>'
    response += HtmlForLed(0) 
    response += HtmlForLed(1) 
    response += HtmlForLed(2) 
    return response

run(host = '0.0.0.0', port = 80)
