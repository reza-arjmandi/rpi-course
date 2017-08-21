from PyQt4 import QtCore, QtGui
from MotorControlModernUi import Ui_Dialog
import RPi.GPIO as GPIO
import sys

enable_pin = 18
in1_pin = 23
in2_pin =24

GPIO.setmode(GPIO.BCM)
GPIO.setup(enable_pin, GPIO.OUT)
GPIO.setup(in1_pin, GPIO.OUT)
GPIO.setup(in2_pin, GPIO.OUT)

pwm = GPIO.PWM(enable_pin, 500)
pwm.start(0)

def clockwise():
	GPIO.output(in1_pin, True)
	GPIO.output(in2_pin, False)

def counter_clockwise():
	GPIO.output(in1_pin, False)
	GPIO.output(in2_pin, True)

class MyGui(QtGui.QWidget):
    def __init__(self, parent=None):
        super(MyGui, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.dial, QtCore.SIGNAL('valueChanged(int)'), self.dialHandler)
        QtCore.QObject.connect(self.ui.CWButton, QtCore.SIGNAL('clicked(bool)'), self.CWHandler)

    def dialHandler(self, value):
        self.ui.progressBar.setValue(value)
        self.ui.lcdNumber.display(value)
        pwm.ChangeDutyCycle(value)

    def CWHandler(self, value):
        if(value == True):
            clockwise()
        else:
            counter_clockwise()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    form = MyGui()
    form.show()
    sys.exit(app.exec_())

