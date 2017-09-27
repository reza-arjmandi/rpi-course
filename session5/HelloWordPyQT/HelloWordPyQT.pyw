######################################################################
#       HelloWordPyQT.pyw
#
# This program create a textBox, button and label in a window 
# and when user clicked on button content of textBox dislay on label.
######################################################################

from PyQt4 import QtCore, QtGui
from gui import Ui_Dialog
import sys

class TestGuiForm(QtGui.QWidget):    
	def __init__(self, parent = None):        
		super(TestGuiForm, self).__init__(parent)        
		self.ui = Ui_Dialog()        
		self.ui.setupUi(self)    
		QtCore.QObject.connect(self.ui.pushButton, QtCore.SIGNAL('clicked()'), 				self.handler)

	def handler(self):
		 self.ui.label.setText(self.ui.lineEdit.text())

if __name__ == '__main__':      
	app = QtGui.QApplication(sys.argv)    
	form = TestGuiForm()    
	form.show()    
	sys.exit(app.exec_())	
