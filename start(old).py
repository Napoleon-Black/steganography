from Tkinter import *
import tkFileDialog
from PIL import ImageTk, Image
import crypt
import re

def Quit(ev):
    global root
    root.quit()
    root.destroy()
    
def LoadFile(ev): 
    fn = tkFileDialog.Open(root).show()
    file_name = re.split(r'/', fn)[-1]
    if fn == '':
        return
    input_file = open(fn, 'r')
    file_str = input_file.read()
    return file_str

def SaveImage(ev):
    fn = tkFileDialog.SaveAs(root, filetypes = [('*.png files', '.png')]).show()
    if fn == '':
        return
    return fn

def SaveFile(ev):
    fn = tkFileDialog.SaveAs(root).show()
    if fn == '':
        return
    return fn

def LoadImage(ev): 
    fn = tkFileDialog.Open(root, filetypes = [('*.png files', '.png')]).show()
    if fn == '':
        return
    return fn
    
def Hide(ev):
    hide_file = LoadFile(0)
    EnterPassword()
    set_image = LoadImage(0)
    password = pwd
    save_to = SaveImage(0)
    crypto = crypt.Crypt()
    crypto.file_crypt(hide_file, set_image, save_to, password)
    

def Unhide(ev):
    crypt_file = LoadImage(0)
    EnterPassword()
    password = pwd
    save_to = SaveFile(0)
    decrypt = crypt.Decrypt()
    decrypt.file_decrypt(crypt_file, password, save_to)


pwd = None

def EnterPassword():

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


hideBtn = Button(panelFrame, text = 'Hide')
unhideBtn = Button(panelFrame, text = 'Unhide')
quitBtn = Button(panelFrame, text = 'Quit')

hideBtn.bind("<Button-1>", Hide)
unhideBtn.bind("<Button-1>", Unhide)
quitBtn.bind("<Button-1>", Quit)

hideBtn.place(x = 0, y = 0, width = 80, height = 30)
unhideBtn.place(x = 0, y = 30, width = 80, height = 30)
quitBtn.place(x = 0, y = 60, width = 80, height = 30)

root.mainloop()
