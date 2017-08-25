# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MotorControlModernUi.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(534, 310)
        self.dial = QtGui.QDial(Dialog)
        self.dial.setGeometry(QtCore.QRect(120, -10, 311, 261))
        self.dial.setMaximum(100)
        self.dial.setObjectName(_fromUtf8("dial"))
        self.lcdNumber = QtGui.QLCDNumber(Dialog)
        self.lcdNumber.setGeometry(QtCore.QRect(10, 250, 71, 41))
        self.lcdNumber.setAutoFillBackground(False)
        self.lcdNumber.setFrameShape(QtGui.QFrame.StyledPanel)
        self.lcdNumber.setFrameShadow(QtGui.QFrame.Raised)
        self.lcdNumber.setDigitCount(3)
        self.lcdNumber.setSegmentStyle(QtGui.QLCDNumber.Filled)
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.progressBar = QtGui.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(90, 250, 441, 41))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 160, 71, 80))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.CWButton = QtGui.QRadioButton(self.groupBox)
        self.CWButton.setGeometry(QtCore.QRect(10, 20, 82, 17))
        self.CWButton.setChecked(True)
        self.CWButton.setObjectName(_fromUtf8("CWButton"))
        self.CCWButton = QtGui.QRadioButton(self.groupBox)
        self.CCWButton.setGeometry(QtCore.QRect(10, 40, 81, 31))
        self.CCWButton.setObjectName(_fromUtf8("CCWButton"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "MotorControl", None))
        self.groupBox.setTitle(_translate("Dialog", "Direction", None))
        self.CWButton.setText(_translate("Dialog", "CW", None))
        self.CCWButton.setText(_translate("Dialog", "CCW", None))

