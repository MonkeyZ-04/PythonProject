from tkinter import *
from tkinter.colorchooser import *
root = Tk()
root.title("My GUI")
root.geometry("500x500")

def selectColor():
    color = askcolor()
    print(color[1])
    myLabel = Label(text="Hello Python",bg=color[1]).pack()


btn = Button(text="Choose Color",command=selectColor).pack()
root.mainloop()
