from Tkinter import *
import tkFileDialog


root = Tk()

def open_file(ev):
    file = tkFileDialog.Open(root, filetypes = [('*.txt files','.txt')]).show()

    if file == '':
        return

def open_button():
    open_file_button = Button(root,
                              text = 'Open file',
                              width = 30, height = 5,
                              bg = 'white', fg = 'black')

    open_file_button.bind('<Button-1>', open_file)

    open_file_button.pack()

open_button()

root.mainloop()
