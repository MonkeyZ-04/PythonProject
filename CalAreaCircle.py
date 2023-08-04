from tkinter import *
root = Tk()
root.title("Program Calculate Circle Area")

# Circle Area = πr2, π = 3.14
Label(text="Radius",font=30).grid(row=0,sticky=W)
radius = IntVar()
et = Entry(width=30,textvariable=radius,font=30)
et.grid(row=0,column=1)

Label(text="CircleArea",font=30).grid(row=1,sticky=W)
et2 = Entry(width=30,font=30)
et2.grid(row=1,column=1)

def calculate():
    r = radius.get()
    area = 3.14*(r**2)
    et2.insert(0,area)
def deleteText():
    et.delete(0,END)
    et2.delete(0,END)

btn1=Button(text="Calculate",command=calculate).grid(row=2,column=1,sticky=W)
btn2=Button(text="Clear",command=deleteText).grid(row=2,column=1,sticky=E)

root.mainloop()