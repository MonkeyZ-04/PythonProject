from tkinter import *

root = Tk()
root.title("My GUI")

# Widget Label
myLabel1 = Label(root,text="Hello World", fg="red", font=20, bg="yellow").pack()

# Button
btn1 = Button(root,text="Click",fg="white",bg="black").pack()

# กำหนดขนาดหน้าจอและตำแหน่งหน้าจอ
root.geometry("500x400+1000+250")
root.mainloop()
