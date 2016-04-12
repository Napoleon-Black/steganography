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

class Ui_Hide(object):
    def setupUi(self, Hide):
        Hide.setObjectName(_fromUtf8("Hide"))
        Hide.setWindowModality(QtCore.Qt.NonModal)
        Hide.resize(350, 250)
        Hide.setMinimumSize(QtCore.QSize(350, 250))
        Hide.setMaximumSize(QtCore.QSize(350, 250))
        Hide.setBaseSize(QtCore.QSize(350, 250))
        self.commandLinkButton = QtGui.QCommandLinkButton(Hide)
        self.commandLinkButton.setGeometry(QtCore.QRect(210, 180, 91, 41))
        self.commandLinkButton.setObjectName(_fromUtf8("commandLinkButton"))
        self.lineEdit = QtGui.QLineEdit(Hide)
        self.lineEdit.setGeometry(QtCore.QRect(20, 30, 201, 20))
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton = QtGui.QPushButton(Hide)
        self.pushButton.setGeometry(QtCore.QRect(230, 29, 75, 23))
        self.pushButton.setStatusTip(_fromUtf8(""))
        self.pushButton.setWhatsThis(_fromUtf8(""))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.lineEdit_2 = QtGui.QLineEdit(Hide)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 81, 201, 20))
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.pushButton_2 = QtGui.QPushButton(Hide)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 80, 75, 23))
        self.pushButton_2.setStatusTip(_fromUtf8(""))
        self.pushButton_2.setWhatsThis(_fromUtf8(""))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(Hide)
        self.pushButton_3.setGeometry(QtCore.QRect(230, 130, 75, 23))
        self.pushButton_3.setStatusTip(_fromUtf8(""))
        self.pushButton_3.setWhatsThis(_fromUtf8(""))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.lineEdit_3 = QtGui.QLineEdit(Hide)
        self.lineEdit_3.setGeometry(QtCore.QRect(20, 131, 201, 20))
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.commandLinkButton_2 = QtGui.QCommandLinkButton(Hide)
        self.commandLinkButton_2.setGeometry(QtCore.QRect(90, 180, 111, 41))
        self.commandLinkButton_2.setObjectName(_fromUtf8("commandLinkButton_2"))

        self.retranslateUi(Hide)
        QtCore.QMetaObject.connectSlotsByName(Hide)

    def retranslateUi(self, Hide):
        Hide.setWindowTitle(_translate("Hide", "Form", None))
        self.commandLinkButton.setText(_translate("Hide", "Hide!", None))
        self.lineEdit.setPlaceholderText(_translate("Hide", "Open file what you want to hide", None))
        self.pushButton.setText(_translate("Hide", "Open File", None))
        self.lineEdit_2.setPlaceholderText(_translate("Hide", "Open your image", None))
        self.pushButton_2.setText(_translate("Hide", "Open Image", None))
        self.pushButton_3.setText(_translate("Hide", "Save as", None))
        self.lineEdit_3.setPlaceholderText(_translate("Hide", "Save as", None))
        self.commandLinkButton_2.setText(_translate("Hide", "Cancel", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Hide = QtGui.QWidget()
    ui = Ui_Hide()
    ui.setupUi(Hide)
    Hide.show()
    sys.exit(app.exec_())

