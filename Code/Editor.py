
import sys 
from tkinter import filedialog
from tkinter import *

root = Tk("Text Editor")
text = Text(root)
text.grid()

def save_as():
    global text
    t = text.get("1.0","end-1c")
    
    savelocation = filedialog.asksaveasfilename()
    file1 = open(savelocation, "w+")
    file1.write(t)
    file1.close()
    
button = Button(root,text = "Save" , command=save_as)
button.grid()

def font_Helvetica():
    global text
    text.config(font = 'Helvetica')

def font_Courier():
    global text
    text.config(font = "Courier")

font = Menubutton(root,text= "Change Font")
font.grid()

font.menu = Menu(font,tearoff=0)
font["menu"] = font.menu
Helvetica = IntVar()
arial=IntVar() 
times=IntVar() 
Courier=IntVar()

font.menu.add_checkbutton(label="Courier",variable = Courier ,command=font_Courier)
font.menu.add_checkbutton(label="Helvetica",variable = Helvetica ,command=font_Helvetica)

root.mainloop()