from tkinter import *

root = Tk()
root.title("My GUI")

# กำหนดขนาดหน้าจอและตำแหน่งหน้าจอ
root.geometry("500x400+1000+250")

# Multi GUI
# myWindow = Tk()
# myWindow.title("Report")
# myWindow.geometry("300x300")


# Button Command
def showMessage():
    # Label(root, text="Hello World", fg="black", font=18).pack()
    msg = txt.get()
    Label(root,text=msg).pack()
    print(msg)
def OpenWindow():
    myWindow = Tk()
    myWindow.title("Report")
    myWindow.geometry("300x300")
    Label(myWindow, text="Hello World", fg="black", font=18).pack()

# Text Box
txt = StringVar()
Entry(root,textvariable=txt).pack()

# Button
btn1 = Button(root,text="Click",fg="white",bg="black",command=showMessage).pack()
btn2 = Button(root,text="OpenNewWindow",fg="white",bg="black",command=OpenWindow).pack()

root.mainloop()
