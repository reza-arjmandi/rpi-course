import sys 
import RPi.GPIO as GPIO
from gui_slider import * 

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
pwm = GPIO.PWM(18, 500)
pwm.start(0)

class MyForm(QtGui.QDialog):  
	def __init__(self, parent=None):    		
		super(MyForm, self).__init__(parent)		
		self.ui = Ui_Dialog()    
		self.ui.setupUi(self)    
		QtCore.QObject.connect(self.ui.slider, QtCore.SIGNAL('valueChanged(int)'),self.dispmessage)  
		
	def dispmessage(self, value):      
		self.ui.PWMLabel.setText(str(value)) 
		pwm.ChangeDutyCycle(float(value))
		
if __name__ == "__main__":   
	app = QtGui.QApplication(sys.argv)   
	myapp = MyForm()   
	myapp.show()   
	sys.exit(app.exec_())