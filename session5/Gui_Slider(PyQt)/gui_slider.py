# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_slider.ui'
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
        Dialog.resize(595, 222)
        self.slider = QtGui.QSlider(Dialog)
        self.slider.setGeometry(QtCore.QRect(30, 100, 451, 22))
        self.slider.setMaximum(100)
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.setObjectName(_fromUtf8("slider"))
        self.PWMLabel = QtGui.QLabel(Dialog)
        self.PWMLabel.setGeometry(QtCore.QRect(510, 100, 47, 13))
        self.PWMLabel.setText(_fromUtf8(""))
        self.PWMLabel.setObjectName(_fromUtf8("PWMLabel"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))

