# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\QT\password.ui'
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

class Ui_EnterPassword(object):
    def setupUi(self, EnterPassword):
        EnterPassword.setObjectName(_fromUtf8("EnterPassword"))
        EnterPassword.resize(295, 100)
        EnterPassword.setMinimumSize(QtCore.QSize(295, 100))
        EnterPassword.setMaximumSize(QtCore.QSize(295, 100))
        EnterPassword.setSizeIncrement(QtCore.QSize(0, 0))
        EnterPassword.setBaseSize(QtCore.QSize(295, 100))
        EnterPassword.setWhatsThis(_fromUtf8(""))
        EnterPassword.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.buttonBox = QtGui.QDialogButtonBox(EnterPassword)
        self.buttonBox.setGeometry(QtCore.QRect(0, 60, 251, 32))
        self.buttonBox.setStatusTip(_fromUtf8(""))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.lineEdit = QtGui.QLineEdit(EnterPassword)
        self.lineEdit.setGeometry(QtCore.QRect(40, 20, 211, 31))
        self.lineEdit.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.lineEdit.setInputMask(_fromUtf8(""))
        self.lineEdit.setText(_fromUtf8(""))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))

        self.retranslateUi(EnterPassword)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), EnterPassword.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), EnterPassword.reject)
        QtCore.QMetaObject.connectSlotsByName(EnterPassword)

    def retranslateUi(self, EnterPassword):
        EnterPassword.setWindowTitle(_translate("EnterPassword", "Enter Password", None))
        EnterPassword.setStatusTip(_translate("EnterPassword", "Enter", None))
        self.lineEdit.setPlaceholderText(_translate("EnterPassword", "Enter your password", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    EnterPassword = QtGui.QDialog()
    ui = Ui_EnterPassword()
    ui.setupUi(EnterPassword)
    EnterPassword.show()
    sys.exit(app.exec_())

