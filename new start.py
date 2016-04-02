from Tkinter import *
import tkFileDialog
from PIL import ImageTk, Image

def Quit(ev):
    global root
    root.destroy()
    
def LoadFile(ev): 
    fn = tkFileDialog.Open(root, filetypes = [('*.txt files', '.txt')]).show()
    if fn == '':
        return

def LoadImage(ev): 
    fn = tkFileDialog.Open(root, filetypes = [('*.jpg files', '.jpg')]).show()
    if fn == '':
        return
    
def Hide(ev):
    pass

def Unhide(ev):
    pass

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