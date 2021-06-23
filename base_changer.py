from tkinter import *


def changer():
    if var.get() == 1:
        number = int(entry.get())
        txt1 = str(number) + " in Binary : " + str(bin(number)[2::])
        txt2 = str(number) + " in Octal : " + str(oct(number)[2::])
        txt3 = str(number) + " in Hexadecimal : " + str(hex(number)[2::])

    elif var.get() == 2:
        number = int(entry.get())
        new_number = int(str(number), 2)
        txt1 = str(number) + " in decimal : " + (str(new_number))
        txt2 = str(number) + " in Octal : " + str(oct(new_number)[2::])
        txt3 = str(number) + " in Hexadecimal : " + str(hex(new_number)[2::])

    elif var.get() == 3:
        number = int(entry.get())
        new_number = int(str(number), 8)
        txt1 = str(number) + " in Binary : " + str(bin(number)[2::])
        txt2 = str(number) + " in decimal : " + (str(new_number))
        txt3 = str(number) + " in Hexadecimal : " + str(hex(new_number)[2::])

    elif var.get() == 4:
        number = int(entry.get())
        new_number = int(str(number), 16)
        txt1 = str(number) + " in Binary : " + str(bin(number)[2::])
        txt2 = str(number) + " in decimal : " + (str(new_number))
        txt3 = str(number) + " in Octal : " + str(oct(new_number)[2::])

    global label1
    global label2
    global label3

    label1 = Label(root, text=txt1)
    label1.grid(row=7, column=0, sticky=W)
    label2 = Label(root, text=txt2)
    label2.grid(row=8, column=0, sticky=W)
    label3 = Label(root, text=txt3)
    label3.grid(row=9, column=0, sticky=W)


def clean():
    label1.destroy()
    label2.destroy()
    label3.destroy()


if __name__ == "__main__":
    root = Tk()
    label = Label(root, text="Number")
    entry = Entry(root)
    label.grid(row=0)
    entry.grid(row=0, column=1)
    var = IntVar()
    Radiobutton(root, text="10", value=1, variable=var).grid(row=1, sticky=W)
    Radiobutton(root, text="2", value=2, variable=var).grid(row=2, sticky=W)
    Radiobutton(root, text="8", value=3, variable=var).grid(row=3, sticky=W)
    Radiobutton(root, text="16", value=4, variable=var).grid(row=4, sticky=W)
    Button(root, text='Show', command=changer).grid(row=5, sticky=W, pady=4)
    Button(root, text='Clean', command=clean).grid(row=6, sticky=W, pady=4)
    root.mainloop()
