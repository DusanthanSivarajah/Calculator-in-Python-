# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 20:19:20 2023

@author: Dusanthan Sivarajah
"""

from tkinter import *


def button_press(num):
    global equation_text 
    
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)

def equals():
    
    try:
        
        global equation_text
        total = str(eval(equation_text))
        
        equation_label.set(total)
        
        equation_text = total
        
    except ZeroDivisionError:
            equation_label.set("Arithmatic Error")
            equation_text=""
    except SyntaxError:
            equation_label.set("Syntax Error")
            equation_text=""

def clear():
    global equation_text
    
    equation_label.set("")
    equation_text=""


    



window = Tk()
window.title("Calculator Program")
window.geometry("350x275")



equation_text = ""

equation_label = StringVar()


label =Label (window, textvariable = equation_label,
              font=('consolas',20),bg="white",width=24,height=2)
label.grid(columnspan=5)





button1 = Button(window, text="1",width=5,font=("Arial",14),command = lambda:button_press(1))
button1.grid(row=1,column=0)

button2 = Button(window, text="2",width=5,font=("Arial",14),command = lambda:button_press(2))
button2.grid(row=1,column=1)

button3 = Button(window, text="3",width=5,font=("Arial",14),command = lambda:button_press(3))
button3.grid(row=1,column=2)

button4 = Button(window, text="4",width=5,font=("Arial",14),command = lambda:button_press(4))
button4.grid(row=2,column=0)

button5 = Button(window, text="5",width=5,font=("Arial",14),command = lambda:button_press(5))
button5.grid(row=2,column=1)

button6 = Button(window, text="6",width=5,font=("Arial",14),command = lambda:button_press(6))
button6.grid(row=2,column=2)

button7 = Button(window, text="7",width=5,font=("Arial",14),command = lambda:button_press(7))
button7.grid(row=3,column=0)

button8 = Button(window, text="8",width=5,font=("Arial",14),command = lambda:button_press(8))
button8.grid(row=3,column=1)

button9 = Button(window, text="9",width=5,font=("Arial",14),command = lambda:button_press(9))
button9.grid(row=3,column=2)

button0 = Button(window, text="0",width=5,font=("Arial",14),command = lambda:button_press(0))
button0.grid(row=4,column=1)

button_plus = Button(window, text="+",width=5,font=("Arial",14),command = lambda:button_press("+"))
button_plus.grid(row=1,column=3)

button_minus = Button(window, text="-",width=5,font=("Arial",14),command = lambda:button_press("-"))
button_minus.grid(row=2,column=3)

button_mul = Button(window, text="*",width=5,font=("Arial",14),command = lambda:button_press("*"))
button_mul.grid(row=3,column=3)

button_div = Button(window, text="/",width=5,font=("Arial",14),command = lambda:button_press("/"))
button_div.grid(row=4,column=3)

button_openbrac = Button(window, text="(",width=5,font=("Arial",14),command = lambda:button_press("("))
button_openbrac.grid(row=5,column=2)

button_closebrac = Button(window, text=")",width=5,font=("Arial",14),command = lambda:button_press(")"))
button_closebrac.grid(row=5,column=3)

button_des = Button(window, text=".",width=5,font=("Arial",14),command = lambda:button_press("."))
button_des.grid(row=4,column=2)

button_cl = Button(window, text="Clear",width=5,font=("Arial",14),command = clear,fg="red")
button_cl.grid(row=4, column=0)

button_eq = Button(window, text="=",width=13,font=("Arial",14),command = equals)
button_eq.grid(row=5,column=0,columnspan=2)




window.mainloop()