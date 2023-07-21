from tkinter import *
from tkinter.colorchooser import *
from tkinter.filedialog import *
root = Tk()
root.title("My GUI")
root.geometry("500x500")

def selectColor():
    color = askcolor()
    print(color[1])
    myLabel = Label(text="Hello Python",bg=color[1]).pack()


def selectFile():
    fileOpen = str(askopenfile())
    fileContent = open(fileOpen,encoding="utf8")
    myLabel = Label(text=fileContent.read()).pack()


btn1 = Button(text="Choose Color",command=selectColor).pack()
btn2 = Button(text="Choose File",command=selectFile).pack()
root.mainloop()
