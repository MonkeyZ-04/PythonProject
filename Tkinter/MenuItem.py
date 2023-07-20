from tkinter import *

root = Tk()
root.title("My GUI")
root.geometry("500x500")

# Menu
myMenu = Menu()
root.config(menu=myMenu)

# Menu Item
menuItem = Menu()
menuItem.add_command(label="MenuItem1")
menuItem.add_command(label="MenuItem2")
menuItem.add_command(label="MenuItem3")

# Add Menu
myMenu.add_cascade(label="Menu1",menu=menuItem)
myMenu.add_cascade(label="Menu2")
myMenu.add_cascade(label="Menu3")



root.mainloop()
