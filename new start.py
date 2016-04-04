from Tkinter import *
import tkFileDialog
import threading
from PIL import ImageTk, Image
import crypt

def Quit(ev):
    global root
    root.quit()
    root.destroy()
    
def LoadFile(ev): 
    fn = tkFileDialog.Open(root).show()
    if fn == '':
        return
    input_file = open(fn, 'r')
    file_str = input_file.read()
    return file_str

def SaveFile(ev):
    fn = tkFileDialog.SaveAs(root).show()
    if fn == '':
        return
    return fn

def LoadImage(ev): 
    fn = tkFileDialog.Open(root, filetypes = [('*.jpg files', '.jpg')]).show()
    if fn == '':
        return
    
def Hide(ev):
<<<<<<< HEAD
=======
    EnterPassword()
    password = ent_password
>>>>>>> f0a4b763f1d9f946e3bb101ed551d75344d1f2f4
    hide_file = LoadFile(0)
    EnterPassword()
    password = pwd
    save_to = SaveFile(0)
    crypto = crypt.Crypt()
    crypto.file_crypt(hide_file, save_to, password)
    

def Unhide(ev):
    crypt_file = LoadFile(0)
    EnterPassword()
    password = pwd
    save_to = SaveFile(0)
    decrypt = crypt.Decrypt()
    decrypt.file_decrypt(crypt_file, password, save_to)

<<<<<<< HEAD
pwd = None

def EnterPassword():
=======
ent_password = None

def EnterPassword():

    def get_pass():
        global ent_password
        if len(password.get()) == 16:
            ent_password = password.get()
            password_window.destroy()

>>>>>>> f0a4b763f1d9f946e3bb101ed551d75344d1f2f4
    password_window = Tk()
    def get_pass():
        global pwd 
        if len(password.get()) == 16:
            pwd = password.get()
            password_window.quit()
            password_window.destroy()
    
    password_window.title('Enter Password')
    password_window.geometry('250x150')

    passFrame = Frame(password_window)
    passFrame.pack()

    lab = Label(passFrame, text = 'Enter Key!')
    lab.grid(row = 0, column = 0, columnspan = 2)

    lab = Label(passFrame, text=' ')
    lab.grid(row=1, column=0, columnspan = 2)

    v = StringVar()
    password = Entry(passFrame, textvariable = v, show = '*', width = 10)
    password.grid(row=2, column=0)

    btpass = Button(passFrame, text = 'Ok', command=get_pass)
    btpass.grid(row=2, column=1)

    kk = StringVar()
    lab = Label(passFrame, text=' ', textvariable = kk)
    lab.grid(row=3, column=0, columnspan = 2)

    btclose = Button(passFrame, text = 'Close', command = lambda : password_window.destroy())
    btclose.grid(row=4, column=1, sticky='e')

    password_window.mainloop()
    

root = Tk()

panelFrame = Frame(root, width = 80, height = 600, bg = 'gray')
textFrame = Frame(root, height = 340, width = 600)

panelFrame.pack(side = 'left', fill = 'x')
textFrame.pack(side = 'bottom', fill = 'both', expand = 1)

textbox = Text(textFrame, font='Arial 14', wrap='word')


textbox.pack(side = 'left', fill = 'both', expand = 1)


loadBtn = Button(panelFrame, text = 'Open file')
imageBtn = Button(panelFrame, text = 'Open image')
hideBtn = Button(panelFrame, text = 'Hide')
unhideBtn = Button(panelFrame, text = 'Unhide')
quitBtn = Button(panelFrame, text = 'Quit')

loadBtn.bind("<Button-1>", LoadFile)
imageBtn.bind("<Button-1>", LoadImage)
hideBtn.bind("<Button-1>", Hide)
unhideBtn.bind("<Button-1>", Unhide)
quitBtn.bind("<Button-1>", Quit)

loadBtn.place(x = 0, y = 0, width = 80, height = 30)
imageBtn.place(x = 0, y = 30, width = 80, height = 30)
hideBtn.place(x = 0, y = 60, width = 80, height = 30)
unhideBtn.place(x = 0, y = 90, width = 80, height = 30)
quitBtn.place(x = 0, y = 120, width = 80, height = 30)

root.mainloop()
