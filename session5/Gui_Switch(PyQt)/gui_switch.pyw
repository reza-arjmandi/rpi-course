######################################################################
#       Gui_Switch.py
#
# This program create a checkBox and control a LED.(PyQt framework) 
######################################################################

import sys 
import RPi.GPIO as GPIO
from gui_switch import * 

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

class MyForm(QtGui.QDialog):  
	def __init__(self, parent=None):    		
		super(MyForm, self).__init__(parent)		
		self.ui = Ui_MainWindow()    
		self.ui.setupUi(self)    
		QtCore.QObject.connect(self.ui.checkBox, QtCore.SIGNAL('clicked(bool)'),self.ToggleLED)  
		
	def ToggleLED(self, value):      
		GPIO.output(18, value)
		
if __name__ == "__main__":   
	app = QtGui.QApplication(sys.argv)   
	myapp = MyForm()   
	myapp.show()   
	sys.exit(app.exec_())