from tkinter import *

root = Tk()
root.title("My GUI")

# Widget Label
myLabel1 = Label(root,text="Hello World", fg="red", font=20, bg="yellow").place(x=100,y=100)
myLabel2 = Label(root,text="row1").grid(row=1,column=0)
myLabel2 = Label(root,text="row2").grid(row=2,column=0)

# กำหนดขนาดหน้าจอและตำแหน่งหน้าจอ
root.geometry("500x400+1000+250")
root.mainloop()
