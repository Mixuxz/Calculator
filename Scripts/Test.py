#Yeet

import tkinter as tk

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    textResult.delete(1.0, "end")
    textResult.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try:
            calculation = str(eval(calculation))
            textResult.delete(1.0, "end")
            textResult.insert(1.0, calculation)


    except:
         clear_field()
         textResult.insert(1.0, "Error")

def clear_field():
    global calculation
    calculation = ""
    textResult.delete(1.0, "end")



root = tk.Tk()
root.geometry("600x400") #ruudun koko, x, y

textResult = tk.Text(root, height = 2, width = 32, font=("Arial", 24))
textResult.grid(columnspan=5)

#Numero napit
btn1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), width=10, font="Arial, 14")
btn1.grid(row=2, column=1)
btn2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), width=10, font="Arial, 14")
btn2.grid(row=2, column=2)
btn3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), width=10, font="Arial, 14")
btn3.grid(row=2, column=3)
btn4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), width=10, font="Arial, 14")
btn4.grid(row=3, column=1)
btn5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), width=10, font="Arial, 14")
btn5.grid(row=3, column=2)
btn6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6), width=10, font="Arial, 14")
btn6.grid(row=3, column=3)
btn7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7), width=10, font="Arial, 14")
btn7.grid(row=4, column=1)
btn8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8), width=10, font="Arial, 14")
btn8.grid(row=4, column=2)
btn9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), width=10, font="Arial, 14")
btn9.grid(row=4, column=3)
btn0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), width=10, font="Arial, 14")
btn0.grid(row=5, column=2)

#functio napit
btnplus = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), width=10, font="Arial, 14")
btnplus.grid(row=2, column=4)
btnmiinus = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), width=10, font="Arial, 14")
btnmiinus.grid(row=3, column=4)
btnkerto = tk.Button(root, text="*", command=lambda: add_to_calculation("*"), width=10, font="Arial, 14")
btnkerto.grid(row=4, column=4)
btnjako = tk.Button(root, text="/", command=lambda: add_to_calculation("/"), width=10, font="Arial, 14")
btnjako.grid(row=5, column=4)
btnauki = tk.Button(root, text="(", command=lambda: add_to_calculation("("), width=10, font="Arial, 14")
btnauki.grid(row=5, column=1)
btnkiini = tk.Button(root, text=")", command=lambda: add_to_calculation(")"), width=10, font="Arial, 14")
btnkiini.grid(row=5, column=3)


btnyht = tk.Button(root, text="=", command=evaluate_calculation, width=12, font="Arial, 14")
btnyht.grid(row=6, column=1, columnspan=2)
btntyh = tk.Button(root, text="C", command= clear_field, width=12, font="Arial, 14")
btntyh.grid(row=6, column=3, columnspan=2)


root.mainloop()