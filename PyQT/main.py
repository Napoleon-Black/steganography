# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from PIL import ImageTk, Image
import crypt, hide, re, sys

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


class Ui_MainWindow(object):

    def Hide(self):
        hide = Ui_Hide()
        start_hide = hide.start_hide_window()
        crypto = crypt.Crypt()
        #crypto.file_crypt(hide_file, set_image, save_to, password)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(640, 480)
        MainWindow.setMinimumSize(QtCore.QSize(640, 480))
        MainWindow.setMaximumSize(QtCore.QSize(640, 480))
        MainWindow.setBaseSize(QtCore.QSize(640, 480))

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setEnabled(True)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 640, 441))
        self.graphicsView.setMaximumSize(QtCore.QSize(640, 480))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName(_fromUtf8("menu"))
        self.menuInfo = QtGui.QMenu(self.menubar)
        self.menuInfo.setObjectName(_fromUtf8("menuInfo"))
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.actionHide = QtGui.QAction(MainWindow)
        self.actionHide.setObjectName(_fromUtf8("actionHide"))
        self.actionHide.setShortcut('Ctrl+H')
        self.actionHide.setStatusTip('Hide file')
        self.actionHide.triggered.connect(self.Hide)

        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionExit.setShortcut('Ctrl+Q')
        self.actionExit.setStatusTip('Exit Application')
        self.actionExit.triggered.connect(QtGui.qApp.quit)

        self.actionUnhide = QtGui.QAction(MainWindow)
        self.actionUnhide.setObjectName(_fromUtf8("actionUnhide"))


        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.menu.addAction(self.actionHide)
        self.menu.addAction(self.actionUnhide)
        self.menu.addSeparator()
        self.menu.addAction(self.actionExit)
        self.menuInfo.addAction(self.actionAbout)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menuInfo.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "StegSystem", None))
        self.menu.setTitle(_translate("MainWindow", "Menu", None))
        self.menuInfo.setTitle(_translate("MainWindow", "Info", None))
        self.actionHide.setText(_translate("MainWindow", "Hide", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionUnhide.setText(_translate("MainWindow", "Unhide", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))


    def start(self):
        app = QtGui.QApplication(sys.argv)
        MainWindow = QtGui.QMainWindow()
        self.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())

class Ui_Hide(object):
    def hideUi(self, Hide):
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


    Hide = QtGui.QWidget()
    self.hideUi(Hide)



if __name__ == '__main__':
    start = Ui_MainWindow()
    start.start()


