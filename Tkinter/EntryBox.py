from tkinter import *
root = Tk()
root.title("Data Entry")
root.geometry("200x200")

Label(text="Name").grid(row=0)
Label(text="Lastname").grid(row=1)
Label(text="PhoneNumber").grid(row=2)

et1 = Entry()
et1.grid(row=0,column=1)
et1.insert(0,"Nonthpawit")

et2 = Entry()
et2.grid(row=1,column=1)
et2.insert(0,"Soongchaiyaphom")

et3 = Entry()
et3.grid(row=2,column=1)
et3.insert(0,"009009009")

def deleteText():
    et1.delete(0,END)
    et2.delete(0, END)
    et3.delete(0, END)

button = Button(text="clear",command=deleteText).grid(row=3,column=1)

root.mainloop()
