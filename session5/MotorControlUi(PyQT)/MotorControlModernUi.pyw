######################################################################
#       MotorControlModernUi.pyw
#
# This program create a attractive user interface for controlling 
# speed and direction of DC motor with L298 chip.(PyQT faramework)
######################################################################

from PyQt4 import QtCore, QtGui
from MotorControlModernUi import Ui_Dialog
import RPi.GPIO as GPIO
import sys

enablePin = 18
in1Pin = 23
in2Pin = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(enablePin, GPIO.OUT)
GPIO.setup(in1Pin, GPIO.OUT)
GPIO.setup(in2Pin, GPIO.OUT)

pwm = GPIO.PWM(enablePin, 500)
pwm.start(0)

def Clockwise():
	GPIO.output(in1Pin, True)
	GPIO.output(in2Pin, False)

def CounterClockwise():
	GPIO.output(in1Pin, False)
	GPIO.output(in2Pin, True)

class MyGui(QtGui.QWidget):
    def __init__(self, parent = None):
        super(MyGui, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.dial, QtCore.SIGNAL('valueChanged(int)'), self.DialHandler)
        QtCore.QObject.connect(self.ui.CWButton, QtCore.SIGNAL('toggled(bool)'), self.CWHandler)

    def DialHandler(self, value):
        self.ui.progressBar.setValue(value)
        self.ui.lcdNumber.display(value)
        pwm.ChangeDutyCycle(int(value))

    def CWHandler(self, value):
        if(value == True):
            Clockwise()
        else:
            CounterClockwise()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    Clockwise()
    form = MyGui()
    form.show()
    sys.exit(app.exec_())

