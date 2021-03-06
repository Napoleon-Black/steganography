# -*- coding: utf-8 -*-

import crypt
import hide
import sys
import os
import re
import unhide

from PIL import Image
from PIL import ImageTk
from PyQt4 import QtCore
from PyQt4 import QtGui


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
        self.combobox_choice = 'None'
        self.combobox_choice2 = 'None'
        self.aes_status = False # default choice for Hide tab
        self.aes_status2 = False # default choice for Unide tab
        self.max_file_size = 1
        self.image_file_type = 'None'
        self.new_image_file = None


    def setupUi(self, MainWindow):

        #initialize Main Window
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setMinimumSize(QtCore.QSize(500, 300))
        MainWindow.setMaximumSize(QtCore.QSize(500, 300))
        self.center_window()

        #add central widget
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setGeometry(QtCore.QRect(0, 0, 500, 300))
        self.centralwidget.setMinimumSize(QtCore.QSize(500, 300))
        self.centralwidget.setMaximumSize(QtCore.QSize(500, 300))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        #add tab widget
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 500, 300))
        self.tabWidget.setMinimumSize(QtCore.QSize(500, 300))
        self.tabWidget.setMaximumSize(QtCore.QSize(500, 300))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))

        #initialize first tab(Hide tab)
        self.hide_tab = QtGui.QWidget()
        self.hide_tab.setObjectName(_fromUtf8("hide_tab"))

        #add text label (Encryption:)
        self.use_aes = QtGui.QLabel(self.hide_tab)
        self.use_aes.setGeometry(QtCore.QRect(40, 30, 106, 21))
        self.use_aes.setObjectName(_fromUtf8("use_aes"))

        #add encryption type box
        self.comboBox = QtGui.QComboBox(self.hide_tab)
        self.comboBox.setGeometry(QtCore.QRect(130, 30, 85, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem('None')
        self.comboBox.addItem('AES')
        self.comboBox.addItem('Blowfish')
        self.comboBox.activated[str].connect(self.onActivated)

        #add text label (Password:)
        self.password_label = QtGui.QLabel(self.hide_tab)
        self.password_label.setGeometry(QtCore.QRect(235, 30, 71, 21))
        self.password_label.setObjectName(_fromUtf8("password_label"))

        #add password input line
        self.password = QtGui.QLineEdit(self.hide_tab)
        self.password.setGeometry(QtCore.QRect(315, 30, 135, 22))
        self.password.setEchoMode(QtGui.QLineEdit.Password)
        self.password.setMaxLength(16)
        self.password.setReadOnly(True)
        self.password.setObjectName(_fromUtf8("password"))
        self.password.textChanged[str].connect(self.get_pass)

        #add text label (Set Image:)
        self.label = QtGui.QLabel(self.hide_tab)
        self.label.setGeometry(QtCore.QRect(45, 70, 81, 21))
        self.label.setObjectName(_fromUtf8("label"))

        #add image address line
        self.lineEdit = QtGui.QLineEdit(self.hide_tab)
        self.lineEdit.setGeometry(QtCore.QRect(130, 70, 235, 20))
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))

        #add image select button
        self.pushButton = QtGui.QPushButton(self.hide_tab)
        self.pushButton.setGeometry(QtCore.QRect(375, 69, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.open_image)

        #add text label (Set File:)
        self.label_2 = QtGui.QLabel(self.hide_tab)
        self.label_2.setGeometry(QtCore.QRect(62, 110, 61, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        #add file address label
        self.lineEdit_2 = QtGui.QLineEdit(self.hide_tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 110, 235, 20))
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))

        #add file select button
        self.pushButton_2 = QtGui.QPushButton(self.hide_tab)
        self.pushButton_2.setGeometry(QtCore.QRect(375, 109, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_2.clicked.connect(self.open_file)

        #add text label (Save to:)
        self.label_3 = QtGui.QLabel(self.hide_tab)
        self.label_3.setGeometry(QtCore.QRect(62, 150, 61, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))

        #add "save to" address line
        self.lineEdit_3 = QtGui.QLineEdit(self.hide_tab)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 150, 235, 20))
        self.lineEdit_3.setText(_fromUtf8(""))
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))

        #add "save to" button
        self.pushButton_3 = QtGui.QPushButton(self.hide_tab)
        self.pushButton_3.setGeometry(QtCore.QRect(375, 150, 75, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_3.clicked.connect(self.image_save_as)

        #add Hide! Button
        self.commandLinkButton = QtGui.QCommandLinkButton(self.hide_tab)
        self.commandLinkButton.setGeometry(QtCore.QRect(350, 190, 101, 41))
        self.commandLinkButton.setObjectName(_fromUtf8("commandLinkButton"))
        self.commandLinkButton.clicked.connect(self.hide)

        self.info_label = QtGui.QLabel(self.hide_tab)
        self.info_label.setGeometry(QtCore.QRect(60, 190, 100, 40))

        #show first tab
        self.tabWidget.addTab(self.hide_tab, _fromUtf8(""))

        #Initialize second tab (Unhide tab)
        self.unhide_tab = QtGui.QWidget()
        self.unhide_tab.setObjectName(_fromUtf8("unhide_tab"))

        #add text label (Encryption:)
        self.use_aes_2 = QtGui.QLabel(self.unhide_tab)
        self.use_aes_2.setGeometry(QtCore.QRect(40, 70, 106, 21))
        self.use_aes_2.setObjectName(_fromUtf8("use_aes_2"))

        #Encryption type box
        self.comboBox2 = QtGui.QComboBox(self.unhide_tab)
        self.comboBox2.setGeometry(QtCore.QRect(130, 70, 85, 22))
        self.comboBox2.setObjectName(_fromUtf8("comboBox"))
        self.comboBox2.addItem('None')
        self.comboBox2.addItem('AES')
        self.comboBox2.addItem('Blowfish')
        self.comboBox2.activated[str].connect(self.onActivated2)

        #add text label (Password:)
        self.password_label_2 = QtGui.QLabel(self.unhide_tab)
        self.password_label_2.setGeometry(QtCore.QRect(235, 70, 71, 21))
        self.password_label_2.setObjectName(_fromUtf8("password_label_2"))
        
        #add password input line
        self.password_2 = QtGui.QLineEdit(self.unhide_tab)
        self.password_2.setGeometry(QtCore.QRect(315, 70, 135, 22))
        self.password_2.setEchoMode(QtGui.QLineEdit.Password)
        self.password_2.setReadOnly(True)
        self.password_2.setMaxLength(16)
        self.password_2.setObjectName(_fromUtf8("password_2"))
        self.password_2.textChanged[str].connect(self.get_pass2)

        #add text label (Set Image:)
        self.label_5 = QtGui.QLabel(self.unhide_tab)
        self.label_5.setGeometry(QtCore.QRect(45, 30, 81, 21))
        self.label_5.setObjectName(_fromUtf8("label_5"))

        #add Image address line
        self.lineEdit_4 = QtGui.QLineEdit(self.unhide_tab)
        self.lineEdit_4.setGeometry(QtCore.QRect(130, 30, 235, 20))
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))

        #add Image select button
        self.pushButton_4 = QtGui.QPushButton(self.unhide_tab)
        self.pushButton_4.setGeometry(QtCore.QRect(375, 29, 75, 23))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_4.clicked.connect(self.open_image2)

        #add text label (Save to:)
        self.label_6 = QtGui.QLabel(self.unhide_tab)
        self.label_6.setGeometry(QtCore.QRect(62, 110, 61, 21))
        self.label_6.setObjectName(_fromUtf8("label_6"))

        #add "save to" address line
        self.lineEdit_5 = QtGui.QLineEdit(self.unhide_tab)
        self.lineEdit_5.setGeometry(QtCore.QRect(130, 110, 235, 20))
        self.lineEdit_5.setText(_fromUtf8(""))
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))

        #add "save to" button
        self.pushButton_5 = QtGui.QPushButton(self.unhide_tab)
        self.pushButton_5.setGeometry(QtCore.QRect(375, 109, 75, 23))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_5.clicked.connect(self.file_save_as)

        #add Unhide! Button
        self.commandLinkButton_2 = QtGui.QCommandLinkButton(self.unhide_tab)
        self.commandLinkButton_2.setGeometry(QtCore.QRect(350, 150, 101, 41))
        self.commandLinkButton_2.setObjectName(_fromUtf8("commandLinkButton_2"))
        self.commandLinkButton_2.clicked.connect(self.unhide)

        self.info_label2 = QtGui.QLabel(self.unhide_tab)
        self.info_label2.setGeometry(QtCore.QRect(60, 170, 100, 40))

        #show second tab
        self.tabWidget.addTab(self.unhide_tab, _fromUtf8(""))

        #set central widget
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
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
        self.use_aes.setText(_translate("MainWindow", "Encryption:", None))
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
        self.use_aes_2.setText(_translate("MainWindow", "Encryption:", 
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
        self.menuMenu.setTitle(_translate("MainWindow", "Menu", None))
        self.menuInfo.setTitle(_translate("MainWindow", "Info", None))
        self.actionHide.setText(_translate("MainWindow", "Hide", None))
        self.actionUnhide.setText(_translate("MainWindow", "Unhide", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))

    # Tab_1 Defs (Hide Tab defs)
    # Open image
    def open_image(self):
        file = QtGui.QFileDialog.getOpenFileName(self.hide_tab, 'Open file', 
                '/home', 'Image Files (*.bmp *.png *.jpg *.jpeg)')
        file = unicode(file)
        if file:
            self.image_file_type = re.findall(r'\w*(\..*)$', file)
            self.image_container = file
            image_x, image_y = (Image.open(self.image_container)).size
            if self.image_file_type[0].lower() == '.png' or \
                self.image_file_type[0].lower() == '.bmp':
                self.max_file_size = (((image_x * image_y)/8)/1000)/8
            else:
                self.max_file_size = ((image_x * image_y)/8)/1000
            self.show_max_size(self.max_file_size)
            self.lineEdit.setText(self.image_container)

    # Open File
    def open_file(self):
        file = QtGui.QFileDialog.getOpenFileName(self.hide_tab, 'Open file', 
                '/home', 'Text Files (*.txt *.rtf *.doc *.docx)')
        file = unicode(file)
        if file:
            self.open_file_adress = file
            self.file_size = (os.path.getsize(self.open_file_adress))/1000.0
            if self.file_size > self.max_file_size:
                self.show_large_file_warning()
            else:
                self.open_file_name = re.findall(r'.*\/(.*)$',self.open_file_adress)
                selected_file = open(file, 'r')
                self.selected_file_str = selected_file.read()
                self.lineEdit_2.setText(self.open_file_adress)
        
    # Save to
    def image_save_as(self):

        if self.image_file_type[0].lower() == '.png':

            filename = QtGui.QFileDialog.getSaveFileName(self.hide_tab, 
                'Save as', '/home', 'PNG Files (*.png)')
            file_type = re.findall(r'\w\.png$|\w\.PNG$', str(filename))

            if file_type:
                self.new_image_file = str(filename)
            else:
                self.new_image_file = str(filename) + '.png'

        elif self.image_file_type[0].lower() == '.jpg' \
                        or self.image_file_type[0].lower() == '.jpeg':

            filename = QtGui.QFileDialog.getSaveFileName(self.hide_tab, 
                        'Save as', '/home', 'JPG Files (*.jpg)')
            file_type = re.findall(r'\w\.jpg$|\w\.JPG$', str(filename))

            if file_type:
                self.new_image_file = str(filename)
            else:
                self.new_image_file = str(filename) + '.jpg'

        elif self.image_file_type[0].lower() == '.bmp':
            filename = QtGui.QFileDialog.getSaveFileName(self.hide_tab, 
                'Save as', '/home', 'BMP Files (*.bmp)')
            file_type = re.findall(r'\w\.bmp$|\w\.BMP$', str(filename))

            if file_type:
                self.new_image_file = str(filename)
            else:
                self.new_image_file = str(filename) + '.bmp'
        
        if self.new_image_file:                
            self.lineEdit_3.setText(self.new_image_file)

    def onActivated(self, choice):
        self.combobox_choice = choice
        if choice == 'None':
            self.password.setReadOnly(True)
        else:
            self.password.setReadOnly(False)


    # Hide
    def hide(self):

        try:
            hide_file = self.selected_file_str
            set_image = self.image_container
            save_to = self.new_image_file
            image_type = self.image_file_type
            file_name = self.open_file_name
            self.status('hide')
            app.processEvents()

            if self.combobox_choice == 'AES':
                password = self.new_password
                crypto = crypt.Crypt()
                crypto.file_crypt(hide_file, set_image, save_to, 
                                  password, image_type, file_name[0])
            elif self.combobox_choice == 'Blowfish':
                password = self.new_password
                crypto = crypt.Crypt()
                crypto.blowfish_file_crypt(hide_file, set_image, save_to, 
                                  password, image_type, file_name[0])
            elif self.combobox_choice == 'None':
                pnghide = hide.HideMessage()
                pnghide.hide_message(hide_file, set_image, save_to,
                                     image_type, file_name[0])

            self.hide_complited()
            self.info_label.setText('')

        except AttributeError:
            self.hide_attribute_error()

    #show status if started hide/unhide
    def status(self, x):
        if x == 'hide':
            self.info_label.setText('     Hiding... \nPlease wait.')
        elif x == 'unhide':
            self.info_label2.setText(' Unhiding... \nPlease wait.')
        app.processEvents()


    # Get Password from password line
    def get_pass(self, password):
        self.new_password = str(password)


    #Tab_2 Defs (Unhide Tab defs)
    #open image
    def open_image2(self):
        file = QtGui.QFileDialog.getOpenFileName(self.hide_tab, 'Open file', 
                '/home', 'Image Files (*.bmp *.png *.jpg *.jpeg)')
        file = unicode(file)
        if file:
            self.image_file_type2 = re.findall(r'\w*(\..*)$', file)
            self.image_container2 = file
            self.lineEdit_4.setText(self.image_container2)


    def onActivated2(self, choice):
        self.combobox_choice2 = choice
        if choice == 'None':
            self.password_2.setReadOnly(True)
        else:
            self.password_2.setReadOnly(False)


    #get password from password line
    def get_pass2(self, password):
        self.new_password2 = str(password)


    # Save to:
    def file_save_as(self):
        directory = QtGui.QFileDialog.getExistingDirectory(MainWindow, 
                                         'Set directory to save file')
        self.new_image_file2 = str(directory)
        self.lineEdit_5.setText(self.new_image_file2)


    # Unhide
    def unhide(self):
        try:
            image_type = self.image_file_type2
            save_to = self.new_image_file2
            crypt_file = self.image_container2
            self.status('unhide')
            app.processEvents()

            if self.combobox_choice2 == 'AES':
                password = self.new_password2
                decrypt = crypt.Decrypt()
                decrypt.file_decrypt(crypt_file, password, save_to, image_type)
                self.unhide_complited()
                self.info_label2.setText('')
            elif self.combobox_choice2 == 'Blowfish':
                password = self.new_password2
                decrypt = crypt.Decrypt()
                decrypt.blowfish_file_decrypt(crypt_file, password, 
                                              save_to, image_type)
                self.unhide_complited()
                self.info_label2.setText('')
            elif self.combobox_choice2 == 'None':
                pngunhide = unhide.UnhideMessage()
                unhiden_file = pngunhide.unhide_message(crypt_file, image_type)

                try:
                    unhiden = open(save_to + '/' + unhiden_file[0], 'w')
                    unhiden.write(unhiden_file[1])
                    unhiden.close()
                    self.unhide_complited()
                except IOError as folder_dir:
                    f_dir = re.findall(r"\'(.*)\'", str(folder_dir))
                    self.permission_denied(f_dir[0])

                self.info_label2.setText('')

        except AttributeError:
            self.unhide_attribute_error()
        

    #About program
    def show_about(self):
        msgBox = QtGui.QMessageBox()
        msgBox.setWindowTitle("About")
        msgBox.setIcon(QtGui.QMessageBox.Information)
        msgBox.setText("     StegSystem    \n")
        msgBox.setInformativeText("    Copyright   2016     "
                                  "\nKit Y., Bogutskii O.")
        msgBox.exec_()


    #Error message if attribute error
    def hide_attribute_error(self):
        msgBox = QtGui.QMessageBox()
        msgBox.setWindowTitle("Error!")
        msgBox.setIcon(QtGui.QMessageBox.Warning)
        msgBox.setText('Error! Please verify:\n\n'
                       '1. Image address\n'
                       '2. File address\n'
                       '3. Save adress\n\n'
                       'If AES status is Enabled. Password must be entered  ')
        msgBox.exec_()


    #Error message if attribute error
    def unhide_attribute_error(self):
        msgBox = QtGui.QMessageBox()
        msgBox.setWindowTitle("Error!")
        msgBox.setIcon(QtGui.QMessageBox.Warning)
        msgBox.setText('Error! Please verify:\n\n'
                       '1. Image address\n'
                       '2. Save adress\n\n'
                       'If AES status is Enabled. Password must be entered  ')
        msgBox.exec_()


    #Error message if permission denied to save folder
    def permission_denied(self, f_dir):
        msgBox = QtGui.QMessageBox()
        msgBox.setWindowTitle("Error! Permission denied!")
        msgBox.setIcon(QtGui.QMessageBox.Critical)
        msgBox.setText('Error! Permission denied to: %s! ' % f_dir)
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

    #Message "File is too large"
    def show_large_file_warning(self):
        msgBox = QtGui.QMessageBox()
        msgBox.setWindowTitle("Warning!")
        msgBox.setIcon(QtGui.QMessageBox.Warning)
        msgBox.setText('Warning! File is too large!\n')
        msgBox.exec_()

    #Show container max size
    def show_max_size(self, size):
        msgBox = QtGui.QMessageBox()
        msgBox.setWindowTitle("Maximum container size")
        msgBox.setIcon(QtGui.QMessageBox.Information)
        msgBox.setText('In this container you can put up to: ' + str(size) + 'Kb')
        msgBox.exec_()  
        

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

