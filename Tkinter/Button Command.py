from tkinter import *

root = Tk()
root.title("My GUI")

# Button Command
def showMessage():
    Label(root, text="Hello World", fg="black", font=18).pack()
    print("Done")
# Widget Label
myLabel1 = Label(root,text="Hello World", fg="red", font=20, bg="yellow").pack()

# Button
btn1 = Button(root,text="Click",fg="white",bg="black",command=showMessage).pack()


# กำหนดขนาดหน้าจอและตำแหน่งหน้าจอ
root.geometry("500x400+1000+250")
root.mainloop()
