# -*- coding: utf-8 -*-

import sys, crypt
from PIL import ImageTk, Image
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

class Ui_MainWindow(object):

    def __init__(self):
        self.combobox_choice = '*.PNG'

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(400, 421)
        MainWindow.setMinimumSize(QtCore.QSize(400, 421))
        MainWindow.setMaximumSize(QtCore.QSize(400, 421))
        MainWindow.setBaseSize(QtCore.QSize(400, 350))

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(400, 380))
        self.centralwidget.setMaximumSize(QtCore.QSize(400, 380))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 400, 380))
        self.tabWidget.setMinimumSize(QtCore.QSize(400, 380))
        self.tabWidget.setMaximumSize(QtCore.QSize(400, 380))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))

        #Tab_1 Code  (Hide tab)
        self.hide_tab = QtGui.QWidget()
        self.hide_tab.setObjectName(_fromUtf8("hide_tab"))

        self.image_type = QtGui.QLabel(self.hide_tab)
        self.image_type.setGeometry(QtCore.QRect(30, 30, 61, 21))
        self.image_type.setObjectName(_fromUtf8("image_type"))

        self.comboBox = QtGui.QComboBox(self.hide_tab)
        self.comboBox.setGeometry(QtCore.QRect(118, 30, 111, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.activated[str].connect(self.onActivated)

        self.use_aes = QtGui.QLabel(self.hide_tab)
        self.use_aes.setGeometry(QtCore.QRect(12, 70, 81, 21))
        self.use_aes.setObjectName(_fromUtf8("use_aes"))
        
        self.checkBox = QtGui.QCheckBox(self.hide_tab)
        self.checkBox.setGeometry(QtCore.QRect(120, 70, 21, 21))
        self.checkBox.setText(_fromUtf8(""))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.checkBox.stateChanged.connect(self.change_encrypt_status)

        self.password = QtGui.QLineEdit(self.hide_tab)
        self.password.setGeometry(QtCore.QRect(120, 110, 113, 20))
        self.password.setEchoMode(QtGui.QLineEdit.Password)
        self.password.setMaxLength(16)
        self.password.setReadOnly(True)
        self.password.setObjectName(_fromUtf8("password"))
        self.password.textChanged[str].connect(self.get_pass)
        self.password_label = QtGui.QLabel(self.hide_tab)
        self.password_label.setGeometry(QtCore.QRect(39, 110, 51, 21))
        self.password_label.setObjectName(_fromUtf8("password_label"))

        self.label = QtGui.QLabel(self.hide_tab)
        self.label.setGeometry(QtCore.QRect(36, 150, 61, 21))
        self.label.setObjectName(_fromUtf8("label"))

        self.lineEdit = QtGui.QLineEdit(self.hide_tab)
        self.lineEdit.setGeometry(QtCore.QRect(120, 150, 113, 20))
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))

        self.pushButton = QtGui.QPushButton(self.hide_tab)
        self.pushButton.setGeometry(QtCore.QRect(250, 149, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.open_image)

        self.label_2 = QtGui.QLabel(self.hide_tab)
        self.label_2.setGeometry(QtCore.QRect(50, 190, 41, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.lineEdit_2 = QtGui.QLineEdit(self.hide_tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 190, 113, 20))
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))

        self.pushButton_2 = QtGui.QPushButton(self.hide_tab)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 190, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_2.clicked.connect(self.open_file)

        self.label_3 = QtGui.QLabel(self.hide_tab)
        self.label_3.setGeometry(QtCore.QRect(48, 230, 41, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.lineEdit_3 = QtGui.QLineEdit(self.hide_tab)
        self.lineEdit_3.setGeometry(QtCore.QRect(120, 230, 113, 20))
        self.lineEdit_3.setText(_fromUtf8(""))
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))

        self.pushButton_3 = QtGui.QPushButton(self.hide_tab)
        self.pushButton_3.setGeometry(QtCore.QRect(250, 230, 75, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_3.clicked.connect(self.image_save_as)

        self.commandLinkButton = QtGui.QCommandLinkButton(self.hide_tab)
        self.commandLinkButton.setGeometry(QtCore.QRect(220, 280, 101, 41))
        self.commandLinkButton.setObjectName(_fromUtf8("commandLinkButton"))
        self.commandLinkButton.clicked.connect(self.hide)

        self.tabWidget.addTab(self.hide_tab, _fromUtf8(""))

        #Tab_2 Code  (Unhide tab)
        self.unhide_tab = QtGui.QWidget()
        self.unhide_tab.setObjectName(_fromUtf8("unhide_tab"))

        self.image_type_2 = QtGui.QLabel(self.unhide_tab)
        self.image_type_2.setGeometry(QtCore.QRect(30, 30, 61, 21))
        self.image_type_2.setObjectName(_fromUtf8("image_type_2"))

        self.comboBox_2 = QtGui.QComboBox(self.unhide_tab)
        self.comboBox_2.setGeometry(QtCore.QRect(118, 30, 111, 22))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox.activated[str].connect(self.onActivated2)

        self.use_aes_2 = QtGui.QLabel(self.unhide_tab)
        self.use_aes_2.setGeometry(QtCore.QRect(12, 70, 81, 21))
        self.use_aes_2.setObjectName(_fromUtf8("use_aes_2"))

        self.checkBox_2 = QtGui.QCheckBox(self.unhide_tab)
        self.checkBox_2.setGeometry(QtCore.QRect(120, 70, 21, 21))
        self.checkBox_2.setText(_fromUtf8(""))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.checkBox.stateChanged.connect(self.change_encrypt_status2)

        self.password_label_2 = QtGui.QLabel(self.unhide_tab)
        self.password_label_2.setGeometry(QtCore.QRect(39, 110, 51, 21))
        self.password_label_2.setObjectName(_fromUtf8("password_label_2"))
        
        self.password_2 = QtGui.QLineEdit(self.unhide_tab)
        self.password_2.setGeometry(QtCore.QRect(120, 110, 113, 20))
        self.password_2.setEchoMode(QtGui.QLineEdit.Normal)
        self.password_2.setReadOnly(True)
        self.password_2.setMaxLength(16)
        self.password_2.setObjectName(_fromUtf8("password_2"))
        self.password.textChanged[str].connect(self.get_pass2)

        self.label_5 = QtGui.QLabel(self.unhide_tab)
        self.label_5.setGeometry(QtCore.QRect(36, 150, 61, 21))
        self.label_5.setObjectName(_fromUtf8("label_5"))

        self.lineEdit_4 = QtGui.QLineEdit(self.unhide_tab)
        self.lineEdit_4.setGeometry(QtCore.QRect(120, 150, 113, 20))
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))

        self.pushButton_4 = QtGui.QPushButton(self.unhide_tab)
        self.pushButton_4.setGeometry(QtCore.QRect(250, 149, 75, 23))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton.clicked.connect(self.open_image2)

        self.label_6 = QtGui.QLabel(self.unhide_tab)
        self.label_6.setGeometry(QtCore.QRect(48, 190, 41, 21))
        self.label_6.setObjectName(_fromUtf8("label_6"))

        self.lineEdit_5 = QtGui.QLineEdit(self.unhide_tab)
        self.lineEdit_5.setGeometry(QtCore.QRect(120, 190, 113, 20))
        self.lineEdit_5.setText(_fromUtf8(""))
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))

        self.pushButton_5 = QtGui.QPushButton(self.unhide_tab)
        self.pushButton_5.setGeometry(QtCore.QRect(250, 190, 75, 23))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton.clicked.connect(self.file_save_as)

        self.commandLinkButton_2 = QtGui.QCommandLinkButton(self.unhide_tab)
        self.commandLinkButton_2.setGeometry(QtCore.QRect(220, 240, 101, 41))
        self.commandLinkButton_2.setObjectName(_fromUtf8("commandLinkButton_2"))
        self.commandLinkButton.clicked.connect(self.unhide)

        self.tabWidget.addTab(self.unhide_tab, _fromUtf8(""))

        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 380, 46, 13))
        self.label_4.setObjectName(_fromUtf8("label_4"))

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))

        self.menuMenu = QtGui.QMenu(self.menubar)
        self.menuMenu.setObjectName(_fromUtf8("menuMenu"))

        self.menuInfo = QtGui.QMenu(self.menubar)
        self.menuInfo.setObjectName(_fromUtf8("menuInfo"))

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))

        MainWindow.setStatusBar(self.statusbar)

        self.actionHide = QtGui.QAction(MainWindow)
        self.actionHide.setObjectName(_fromUtf8("actionHide"))

        self.actionUnhide = QtGui.QAction(MainWindow)
        self.actionUnhide.setObjectName(_fromUtf8("actionUnhide"))

        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))

        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))

        self.menuMenu.addAction(self.actionHide)
        self.menuMenu.addAction(self.actionUnhide)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionExit)
        self.menuInfo.addAction(self.actionAbout)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuInfo.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "StegSystem", None))
        self.image_type.setText(_translate("MainWindow", "Image type:", None))
        self.comboBox.setItemText(0, _translate("MainWindow", "*.PNG", None))
        self.comboBox.setItemText(1, _translate("MainWindow", "*.JPG", None))
        self.comboBox.setItemText(2, _translate("MainWindow", "*.BMP", None))
        self.use_aes.setText(_translate("MainWindow", "AES Encryption:", None))
        self.password.setPlaceholderText(_translate("MainWindow", "Enter password", None))
        self.password_label.setText(_translate("MainWindow", "Password:", None))
        self.label.setText(_translate("MainWindow", "Set Image:", None))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Image dir", None))
        self.pushButton.setText(_translate("MainWindow", "Select", None))
        self.label_2.setText(_translate("MainWindow", "Set File:", None))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Set file to hide", None))
        self.pushButton_2.setText(_translate("MainWindow", "Select", None))
        self.label_3.setText(_translate("MainWindow", "Save to:", None))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "Save new image to", None))
        self.pushButton_3.setText(_translate("MainWindow", "Select", None))
        self.commandLinkButton.setText(_translate("MainWindow", "Hide!", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.hide_tab), _translate("MainWindow", "Hide", None))
        self.image_type_2.setText(_translate("MainWindow", "Image type:", None))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "*.PNG", None))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "*.JPG", None))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "*.BMP", None))
        self.use_aes_2.setText(_translate("MainWindow", "AES Encryption:", None))
        self.password_label_2.setText(_translate("MainWindow", "Password:", None))
        self.password_2.setPlaceholderText(_translate("MainWindow", "Enter password", None))
        self.label_5.setText(_translate("MainWindow", "Set Image:", None))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "Image dir", None))
        self.pushButton_4.setText(_translate("MainWindow", "Select", None))
        self.label_6.setText(_translate("MainWindow", "Save to:", None))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "Save unhiden file to", None))
        self.pushButton_5.setText(_translate("MainWindow", "Select", None))
        self.commandLinkButton_2.setText(_translate("MainWindow", "Unhide!", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.unhide_tab), _translate("MainWindow", "Unhide", None))
        self.label_4.setText(_translate("MainWindow", "TextLabel", None))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu", None))
        self.menuInfo.setTitle(_translate("MainWindow", "Info", None))
        self.actionHide.setText(_translate("MainWindow", "Hide", None))
        self.actionUnhide.setText(_translate("MainWindow", "Unhide", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))

    # Tab_1 Defs (Hide Tab defs)
    def open_image(self):
        if self.combobox_choice == '*.PNG':
            file = QtGui.QFileDialog.getOpenFileName(self.hide_tab, 'Open file', 
                '/home', 'PNG Files (*.png)')
        elif self.combobox_choice == '*.JPG':
            file = QtGui.QFileDialog.getOpenFileName(self.hide_tab, 'Open file', 
                '/home', 'JPG Files (*.jpg)')
        elif self.combobox_choice == '*.BMP':
            file = QtGui.QFileDialog.getOpenFileName(self.hide_tab, 'Open file', 
                '/home', 'BMP Files (*.bmp)')
        self.image_container = str(file)

    def open_file(self):
        file = QtGui.QFileDialog.getOpenFileName(self.hide_tab, 'Open file', 
                '/home', 'Text Files (*.txt)')
        selected_file = open(str(file), 'r')
        self.selected_file_str = selected_file.read()
        

    def image_save_as(self):
        filename = QtGui.QFileDialog.getSaveFileName(self.hide_tab, 'Save as',
                '/home', 'PNG Files (*.png)')
        self.new_image_file = str(filename) + '.png'

    def onActivated(self, choice):
        self.combobox_choice = choice

    def change_encrypt_status(self, state):
        if state != QtCore.Qt.Checked:
            self.password.setReadOnly(True)
        else:
            self.password.setReadOnly(False)

    def hide(self):
        hide_file = self.selected_file_str
        set_image = self.image_container
        save_to = self.new_image_file
        password = self.new_password
        crypto = crypt.Crypt()
        crypto.file_crypt(hide_file, set_image, save_to, password)

    def get_pass(self, password):
        self.new_password = str(password)


    #Tab_2 Defs (Unhide Tab defs)

    def open_image2(self):
        if self.combobox_choice2 == '*.PNG':
            file = QtGui.QFileDialog.getOpenFileName(self.hide_tab, 'Open file', 
                '/home', 'PNG Files (*.png)')
        elif self.combobox_choice2 == '*.JPG':
            file = QtGui.QFileDialog.getOpenFileName(self.hide_tab, 'Open file', 
                '/home', 'JPG Files (*.jpg)')
        elif self.combobox_choice2 == '*.BMP':
            file = QtGui.QFileDialog.getOpenFileName(self.hide_tab, 'Open file', 
                '/home', 'BMP Files (*.bmp)')
        self.image_container2 = str(file)

    def onActivated2(self, choice):
        self.combobox_choice2 = choice

    def change_encrypt_status2(self, state):
        if state != QtCore.Qt.Checked:
            self.password_2.setReadOnly(True)
        else:
            self.password_2.setReadOnly(False)

    def get_pass2(self, password):
        self.new_password2 = str(password)

    def file_save_as(self):
        filename = QtGui.QFileDialog.getSaveFileName(self.hide_tab, 'Save as',
                '/home', 'Text Files (*.txt)')
        self.new_image_file2 = str(filename) + '.txt'

    def unhide(self):
        crypt_file = self.open_image2
        password = self.new_password2
        save_to = self.file_save_as
        decrypt = crypt.Decrypt()
        decrypt.file_decrypt(crypt_file, password, save_to)
        

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

