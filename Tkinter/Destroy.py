from tkinter import *
import tkinter.messagebox

root = Tk()
root.title("My GUI")
root.geometry("500x500")

# Menu
myMenu = Menu()
root.config(menu=myMenu)


def ShowWindow():
    window = Tk()
    window.title("NewWindow")
    window.mainloop()


def aboutprogram():
    tkinter.messagebox.showinfo("AboutProgram", "OG:MonkeyZ")


def exitprogram():
    confirm = tkinter.messagebox.askquestion("Exit", "Do you want to exit?")
    if confirm == "yes":
        root.destroy()
    else:
        pass

# Menu Item
menuItem = Menu()
menuItem.add_command(label="New Window", command=ShowWindow)
menuItem.add_command(label="Open")
menuItem.add_command(label="Save")
menuItem.add_command(label="About", command=aboutprogram)
menuItem.add_command(label="Exit", command=exitprogram)

# Add Menu
myMenu.add_cascade(label="File", menu=menuItem)
myMenu.add_cascade(label="Edit")
myMenu.add_cascade(label="View")

root.mainloop()
