from tkinter import *

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

# Menu Item
menuItem = Menu()
menuItem.add_command(label="New Window", command=ShowWindow)
menuItem.add_command(label="Open")
menuItem.add_command(label="Save")

# Add Menu
myMenu.add_cascade(label="File",menu=menuItem)
myMenu.add_cascade(label="Edit")
myMenu.add_cascade(label="View")



root.mainloop()
