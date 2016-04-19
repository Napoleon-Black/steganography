# -*- coding: utf-8 -*-

import sys, re, crypt, png_hide, png_unhide
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
        self.combobox_choice = '*.PNG' # default choice for Hide tab
        self.combobox_choice2 = '*.PNG' # default choice for Unide tab
        self.aes_status = False # default choice for Hide tab
        self.aes_status2 = False # default choice for Unide tab


    def setupUi(self, MainWindow):

        #initialize Main Window
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(400, 421)
        MainWindow.setMinimumSize(QtCore.QSize(400, 421))
        MainWindow.setMaximumSize(QtCore.QSize(400, 421))
        MainWindow.setBaseSize(QtCore.QSize(400, 350))
        self.center_window()

        #add central widget
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(400, 380))
        self.centralwidget.setMaximumSize(QtCore.QSize(400, 380))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        #add tab widget
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 400, 380))
        self.tabWidget.setMinimumSize(QtCore.QSize(400, 380))
        self.tabWidget.setMaximumSize(QtCore.QSize(400, 380))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))

        #initialize first tab(Hide tab)
        self.hide_tab = QtGui.QWidget()
        self.hide_tab.setObjectName(_fromUtf8("hide_tab"))

        #add text label (Image type:)
        self.image_type = QtGui.QLabel(self.hide_tab)
        self.image_type.setGeometry(QtCore.QRect(35, 30, 81, 21))
        self.image_type.setObjectName(_fromUtf8("image_type"))

        #add combo box with image formats
        self.comboBox = QtGui.QComboBox(self.hide_tab)
        self.comboBox.setGeometry(QtCore.QRect(130, 30, 120, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.activated[str].connect(self.onActivated)

        #add text label (AES Encryption:)
        self.use_aes = QtGui.QLabel(self.hide_tab)
        self.use_aes.setGeometry(QtCore.QRect(10, 70, 106, 21))
        self.use_aes.setObjectName(_fromUtf8("use_aes"))
        
        #add aes encryption checkbox
        self.checkBox = QtGui.QCheckBox(self.hide_tab)
        self.checkBox.setGeometry(QtCore.QRect(130, 70, 21, 21))
        self.checkBox.setText(_fromUtf8(""))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.checkBox.stateChanged.connect(self.change_encrypt_status)

        #add password input line
        self.password = QtGui.QLineEdit(self.hide_tab)
        self.password.setGeometry(QtCore.QRect(130, 110, 120, 22))
        self.password.setEchoMode(QtGui.QLineEdit.Password)
        self.password.setMaxLength(16)
        self.password.setReadOnly(True)
        self.password.setObjectName(_fromUtf8("password"))
        self.password.textChanged[str].connect(self.get_pass)

        #add text label (Password:)
        self.password_label = QtGui.QLabel(self.hide_tab)
        self.password_label.setGeometry(QtCore.QRect(48, 110, 71, 21))
        self.password_label.setObjectName(_fromUtf8("password_label"))

        #add text label (Set Image:)
        self.label = QtGui.QLabel(self.hide_tab)
        self.label.setGeometry(QtCore.QRect(45, 150, 81, 21))
        self.label.setObjectName(_fromUtf8("label"))

        #add image address line
        self.lineEdit = QtGui.QLineEdit(self.hide_tab)
        self.lineEdit.setGeometry(QtCore.QRect(130, 150, 170, 20))
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))

        #add image select button
        self.pushButton = QtGui.QPushButton(self.hide_tab)
        self.pushButton.setGeometry(QtCore.QRect(310, 149, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.open_image)

        #add text label (Set File:)
        self.label_2 = QtGui.QLabel(self.hide_tab)
        self.label_2.setGeometry(QtCore.QRect(62, 190, 61, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        #add file address label
        self.lineEdit_2 = QtGui.QLineEdit(self.hide_tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 190, 170, 20))
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))

        #add file select button
        self.pushButton_2 = QtGui.QPushButton(self.hide_tab)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 190, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_2.clicked.connect(self.open_file)

        #add text label (Save to:)
        self.label_3 = QtGui.QLabel(self.hide_tab)
        self.label_3.setGeometry(QtCore.QRect(62, 230, 61, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))

        #add "save to" address line
        self.lineEdit_3 = QtGui.QLineEdit(self.hide_tab)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 230, 170, 20))
        self.lineEdit_3.setText(_fromUtf8(""))
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))

        #add "save to" button
        self.pushButton_3 = QtGui.QPushButton(self.hide_tab)
        self.pushButton_3.setGeometry(QtCore.QRect(310, 230, 75, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_3.clicked.connect(self.image_save_as)

        #add Hide! Button
        self.commandLinkButton = QtGui.QCommandLinkButton(self.hide_tab)
        self.commandLinkButton.setGeometry(QtCore.QRect(220, 280, 101, 41))
        self.commandLinkButton.setObjectName(_fromUtf8("commandLinkButton"))
        self.commandLinkButton.clicked.connect(self.hide)

        #show first tab
        self.tabWidget.addTab(self.hide_tab, _fromUtf8(""))

        #Initialize second tab (Unhide tab)
        self.unhide_tab = QtGui.QWidget()
        self.unhide_tab.setObjectName(_fromUtf8("unhide_tab"))

        #add text label (Image type)
        self.image_type_2 = QtGui.QLabel(self.unhide_tab)
        self.image_type_2.setGeometry(QtCore.QRect(35, 30, 81, 21))
        self.image_type_2.setObjectName(_fromUtf8("image_type_2"))

        #add combobox with image formats
        self.comboBox_2 = QtGui.QComboBox(self.unhide_tab)
        self.comboBox_2.setGeometry(QtCore.QRect(130, 30, 120, 22))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.activated[str].connect(self.onActivated2)

        #add text label (AES Encryption:)
        self.use_aes_2 = QtGui.QLabel(self.unhide_tab)
        self.use_aes_2.setGeometry(QtCore.QRect(10, 70, 106, 21))
        self.use_aes_2.setObjectName(_fromUtf8("use_aes_2"))

        #add aes encryption checkbox
        self.checkBox_2 = QtGui.QCheckBox(self.unhide_tab)
        self.checkBox_2.setGeometry(QtCore.QRect(130, 70, 21, 21))
        self.checkBox_2.setText(_fromUtf8(""))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.checkBox_2.stateChanged.connect(self.change_encrypt_status2)

        #add text label (Password:)
        self.password_label_2 = QtGui.QLabel(self.unhide_tab)
        self.password_label_2.setGeometry(QtCore.QRect(48, 110, 71, 21))
        self.password_label_2.setObjectName(_fromUtf8("password_label_2"))
        
        #add password input line
        self.password_2 = QtGui.QLineEdit(self.unhide_tab)
        self.password_2.setGeometry(QtCore.QRect(130, 110, 120, 22))
        self.password_2.setEchoMode(QtGui.QLineEdit.Password)
        self.password_2.setReadOnly(True)
        self.password_2.setMaxLength(16)
        self.password_2.setObjectName(_fromUtf8("password_2"))
        self.password_2.textChanged[str].connect(self.get_pass2)

        #add text label (Set Image:)
        self.label_5 = QtGui.QLabel(self.unhide_tab)
        self.label_5.setGeometry(QtCore.QRect(45, 150, 81, 21))
        self.label_5.setObjectName(_fromUtf8("label_5"))

        #add Image address line
        self.lineEdit_4 = QtGui.QLineEdit(self.unhide_tab)
        self.lineEdit_4.setGeometry(QtCore.QRect(130, 150, 170, 20))
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))

        #add Image select button
        self.pushButton_4 = QtGui.QPushButton(self.unhide_tab)
        self.pushButton_4.setGeometry(QtCore.QRect(310, 149, 75, 23))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_4.clicked.connect(self.open_image2)

        #add text label (Save to:)
        self.label_6 = QtGui.QLabel(self.unhide_tab)
        self.label_6.setGeometry(QtCore.QRect(62, 190, 61, 21))
        self.label_6.setObjectName(_fromUtf8("label_6"))

        #add "save to" address line
        self.lineEdit_5 = QtGui.QLineEdit(self.unhide_tab)
        self.lineEdit_5.setGeometry(QtCore.QRect(130, 190, 170, 20))
        self.lineEdit_5.setText(_fromUtf8(""))
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))

        #add "save to" button
        self.pushButton_5 = QtGui.QPushButton(self.unhide_tab)
        self.pushButton_5.setGeometry(QtCore.QRect(310, 190, 75, 23))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_5.clicked.connect(self.file_save_as)

        #add Unhide! Button
        self.commandLinkButton_2 = QtGui.QCommandLinkButton(self.unhide_tab)
        self.commandLinkButton_2.setGeometry(QtCore.QRect(220, 240, 101, 41))
        self.commandLinkButton_2.setObjectName(_fromUtf8("commandLinkButton_2"))
        self.commandLinkButton_2.clicked.connect(self.unhide)

        #show second tab
        self.tabWidget.addTab(self.unhide_tab, _fromUtf8(""))

        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 380, 46, 13))
        self.label_4.setObjectName(_fromUtf8("label_4"))

        #set central widget
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))

        self.menuMenu = QtGui.QMenu(self.menubar)
        self.menuMenu.setObjectName(_fromUtf8("menuMenu"))

        self.menuInfo = QtGui.QMenu(self.menubar)
        self.menuInfo.setObjectName(_fromUtf8("menuInfo"))

        #set Menu Bar
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))

        #set Status Bar
        MainWindow.setStatusBar(self.statusbar)

        #hide menu button
        self.actionHide = QtGui.QAction(MainWindow)
        self.actionHide.setObjectName(_fromUtf8("actionHide"))
        self.actionHide.setShortcut('Ctrl+H')
        self.actionHide.triggered.connect(lambda x: self.tabWidget.\
                                          setCurrentIndex(0))
        #unhide menu button
        self.actionUnhide = QtGui.QAction(MainWindow)
        self.actionUnhide.setObjectName(_fromUtf8("actionUnhide"))
        self.actionUnhide.setShortcut('Ctrl+U')
        self.actionUnhide.triggered.connect(lambda x: self.tabWidget.\
                                            setCurrentIndex(1))
        #exit menu button
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionExit.setShortcut('Ctrl+Q')
        self.actionExit.setStatusTip('Exit application')
        self.actionExit.triggered.connect(lambda x: app.quit())
        
        #about menu button
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionAbout.triggered.connect(self.show_about)

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

    #translation
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "StegSystem", None))
        self.image_type.setText(_translate("MainWindow", "Image type:", None))
        self.comboBox.setItemText(0, _translate("MainWindow", "*.PNG", None))
        self.comboBox.setItemText(1, _translate("MainWindow", "*.JPG", None))
        self.comboBox.setItemText(2, _translate("MainWindow", "*.BMP", None))
        self.use_aes.setText(_translate("MainWindow", "AES Encryption:", None))
        self.password.setPlaceholderText(_translate("MainWindow", 
                                         "Enter password", None))
        self.password_label.setText(_translate("MainWindow", "Password:", None))
        self.label.setText(_translate("MainWindow", "Set Image:", None))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", 
                                        "Image dir", None))
        self.pushButton.setText(_translate("MainWindow", "Select", None))
        self.label_2.setText(_translate("MainWindow", "Set File:", None))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", 
                                            "Set file to hide", None))
        self.pushButton_2.setText(_translate("MainWindow", "Select", None))
        self.label_3.setText(_translate("MainWindow", "Save to:", None))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", 
                                            "Save new image to", None))
        self.pushButton_3.setText(_translate("MainWindow", "Select", None))
        self.commandLinkButton.setText(_translate("MainWindow", "Hide!", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.hide_tab), 
                                  _translate("MainWindow", "Hide", None))
        self.image_type_2.setText(_translate("MainWindow", "Image type:", None))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "*.PNG", None))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "*.JPG", None))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "*.BMP", None))
        self.use_aes_2.setText(_translate("MainWindow", "AES Encryption:", 
                                            None))
        self.password_label_2.setText(_translate("MainWindow", "Password:", 
                                            None))
        self.password_2.setPlaceholderText(_translate("MainWindow", 
                                            "Enter password", None))
        self.label_5.setText(_translate("MainWindow", "Set Image:", None))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", 
                                            "Image dir", None))
        self.pushButton_4.setText(_translate("MainWindow", "Select", None))
        self.label_6.setText(_translate("MainWindow", "Save to:", None))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", 
                                            "Save unhiden file to", None))
        self.pushButton_5.setText(_translate("MainWindow", "Select", None))
        self.commandLinkButton_2.setText(_translate("MainWindow", 
                                        "Unhide!", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.unhide_tab), 
                                 _translate("MainWindow", "Unhide", None))
        self.label_4.setText(_translate("MainWindow", "TextLabel", None))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu", None))
        self.menuInfo.setTitle(_translate("MainWindow", "Info", None))
        self.actionHide.setText(_translate("MainWindow", "Hide", None))
        self.actionUnhide.setText(_translate("MainWindow", "Unhide", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))

    # Tab_1 Defs (Hide Tab defs)
    # Open image
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
        self.lineEdit.setText(self.image_container)

    # Open File
    def open_file(self):
        file = QtGui.QFileDialog.getOpenFileName(self.hide_tab, 'Open file', 
                '/home', 'Text Files (*.txt)')
        self.open_file_adress = str(file)
        selected_file = open(str(file), 'r')
        self.selected_file_str = selected_file.read()
        self.lineEdit_2.setText(self.open_file_adress)
        
    # Save to
    def image_save_as(self):
        filename = QtGui.QFileDialog.getSaveFileName(self.hide_tab, 'Save as',
                '/home', 'PNG Files (*.png)')
        file_type = re.findall(r'\w\.png$|\w\.PNG$', str(filename))
        if file_type:
            self.new_image_file = str(filename)
        else:
            self.new_image_file = str(filename) + '.png'
        self.lineEdit_3.setText(self.new_image_file)

    #Set Image type
    def onActivated(self, choice):
        self.combobox_choice = choice

    # Set AES encryption status (On/Off)
    def change_encrypt_status(self, state):
        if state == QtCore.Qt.Checked:
            self.password.setReadOnly(False)
            self.aes_status = True
        else:
            self.password.setReadOnly(True)
            self.aes_status = False

    # Hide
    def hide(self):
        if self.aes_status == True:
            hide_file = self.selected_file_str
            set_image = self.image_container
            save_to = self.new_image_file
            password = self.new_password
            crypto = crypt.Crypt()
            crypto.file_crypt(hide_file, set_image, save_to, password)
        else:
            hide_file = self.selected_file_str
            set_image = self.image_container
            save_to = self.new_image_file
            pnghide = png_hide.HideMessage()
            pnghide.hide_message(hide_file, set_image, save_to)
        self.hide_complited()

    # Get Password from password line
    def get_pass(self, password):
        self.new_password = str(password)


    #Tab_2 Defs (Unhide Tab defs)
    #open image
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
        self.lineEdit_4.setText(self.image_container2)

    #set image type
    def onActivated2(self, choice):
        self.combobox_choice2 = choice

    #set AES Encryption status (On/Off)
    def change_encrypt_status2(self, state):
        if state == QtCore.Qt.Checked:
            self.password_2.setReadOnly(False)
            self.aes_status2 = True
        else:
            self.password_2.setReadOnly(True)
            self.aes_status2 = False

    #get password from password line
    def get_pass2(self, password):
        self.new_password2 = str(password)

    # Save to:
    def file_save_as(self):
        filename = QtGui.QFileDialog.getSaveFileName(self.hide_tab, 'Save as',
                '/home', 'Text Files (*.txt)')
        file_type = re.findall(r'\w\.txt$|\w\.TXT$', str(filename))
        if file_type:
            self.new_image_file2 = str(filename)
        else:
            self.new_image_file2 = str(filename) + '.txt'
        self.lineEdit_5.setText(self.new_image_file2)

    # Unhide
    def unhide(self):
        if self.aes_status2 == True:
            crypt_file = self.image_container2
            save_to = self.new_image_file2
            password = self.new_password2
            decrypt = crypt.Decrypt()
            decrypt.file_decrypt(crypt_file, password, save_to)
        else:
            hiden_file = self.image_container2
            save_to = self.new_image_file2
            pngunhide = png_unhide.UnhideMessage()
            unhiden_file = pngunhide.unhide_message(hiden_file)
            unhiden = open(save_to, 'w')
            unhiden.write(unhiden_file)
            unhiden.close()
        self.unhide_complited()

    #About program
    def show_about(self):
        msgBox = QtGui.QMessageBox()
        msgBox.setWindowTitle("About")
        msgBox.setIcon(QtGui.QMessageBox.Information)
        msgBox.setText("     StegSystem    \n")
        msgBox.setInformativeText("    Copyright   2016     "
                                  "\nKit Y., Bogutskii O.")
        msgBox.exec_()

    #Center Window
    def center_window(self):
        resolution = QtGui.QDesktopWidget().screenGeometry()
        my_size = MainWindow.geometry()
        width = ( resolution.width() - my_size.width() ) / 2
        height = ( resolution.height() - my_size.height() ) / 2
        MainWindow.move(width, height)

    #Message "Hide Complited" 
    def hide_complited(self):
        msgBox = QtGui.QMessageBox()
        msgBox.setWindowTitle("Complited!")
        msgBox.setIcon(QtGui.QMessageBox.Information)
        msgBox.setText('Hiding data complited')
        msgBox.exec_()

    #Message "Unhide Complited" 
    def unhide_complited(self):
        msgBox = QtGui.QMessageBox()
        msgBox.setWindowTitle("Complited!")
        msgBox.setIcon(QtGui.QMessageBox.Information)
        msgBox.setText('Unhiding data complited')
        msgBox.exec_()
        
        


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

