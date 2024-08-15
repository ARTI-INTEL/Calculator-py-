from tkinter import *

root = Tk()
root.title("Simple Calculator")

display = Entry(root, width=35, borderwidth=5)
display.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

calc = [0,"",0]

def btn_click(var):
    val = display.get()
    var = str(var)
    display.delete(0, END)
    display.insert(0, val+var)

def btn_clear():
    global calc
    calc = [0,"",0]
    display.delete(0, END)

def btn_delete():
    val = display.get()
    val = val[:-1]
    display.insert(0, val)

def btn_calculate():
    equation = display.get()
    display.delete(0, END)
    display.insert(0, eval(equation))


#Declare Buttons
btn1 = Button(root, text="1", padx=40, pady=20, command=lambda: btn_click(1))
btn2 = Button(root, text="2", padx=40, pady=20, command=lambda: btn_click(2))
btn3 = Button(root, text="3", padx=40, pady=20, command=lambda: btn_click(3))

btn4 = Button(root, text="4", padx=40, pady=20, command=lambda: btn_click(4))
btn5 = Button(root, text="5", padx=40, pady=20, command=lambda: btn_click(5))
btn6 = Button(root, text="6", padx=40, pady=20, command=lambda: btn_click(6))

btn7 = Button(root, text="7", padx=40, pady=20, command=lambda: btn_click(7))
btn8 = Button(root, text="8", padx=40, pady=20, command=lambda: btn_click(8))
btn9 = Button(root, text="9", padx=40, pady=20, command=lambda: btn_click(9))

btn0 = Button(root, text="0", padx=40, pady=20, command=lambda: btn_click(0))
btn_sub = Button(root, text="-", padx=40, pady=20, command=lambda: btn_click("-"))
btn_add = Button(root, text="+", padx=40, pady=20, command=lambda: btn_click("+"))

btn_div = Button(root, text="/", padx=40, pady=20, command=lambda: btn_click("*"))
btn_multi = Button(root, text="*", padx=40, pady=20, command=lambda: btn_click("/"))
btn_del = Button(root, text="DEL", padx=40, pady=20, command=btn_delete)

btn_clr = Button(root, text="C", padx=40, pady=20, command=btn_clear)
btn_equal = Button(root, text="=", padx=80, pady=20, command=btn_calculate)


#Position Buttons
btn1.grid(row=3, column=0)
btn2.grid(row=3, column=1)
btn3.grid(row=3, column=2)

btn4.grid(row=2, column=0)
btn5.grid(row=2, column=1)
btn6.grid(row=2, column=2)

btn7.grid(row=1, column=0)
btn8.grid(row=1, column=1)
btn9.grid(row=1, column=2)

btn0.grid(row=4, column=0)
btn_sub.grid(row=4, column=1)
btn_add.grid(row=4, column=2)

btn_div.grid(row=5, column=0)
btn_multi.grid(row=5, column=1)
btn_del.grid(row=5, column=2)

btn_clr.grid(row=6, column=0)
btn_equal.grid(row=6, column=1, columnspan=2)

root.mainloop()