from tkinter import *
import math

root = Tk()   
root.geometry("650x500+300+200")
root.title("Scientific Calculator")

# Display
disp = Entry(root, font=("Verdana", 20), fg="black", bg="mistyrose", bd=8, justify=RIGHT)
disp.grid(row=0, column=0, columnspan=6, pady=10, sticky="nsew")

# Button click handler
def btn_click(item):
    current = disp.get()
    disp.delete(0, END)
    disp.insert(END, current + str(item))

def clear_disp():
    disp.delete(0, END)

def evaluate():
    try:
        expression = disp.get()
        # Replace math functions
        expression = expression.replace("π", str(math.pi))
        expression = expression.replace("sin", "math.sin")
        expression = expression.replace("cos", "math.cos")
        expression = expression.replace("tan", "math.tan")
        expression = expression.replace("log", "math.log10")
        expression = expression.replace("ln", "math.log")
        expression = expression.replace("√", "math.sqrt")
        expression = expression.replace("^", "**")
        result = eval(expression)
        disp.delete(0, END)
        disp.insert(END, str(result))
    except Exception:
        disp.delete(0, END)
        disp.insert(END, "Error")

# Scientific buttons
scientific_buttons = [
    ["π", "x!", "sin", "cos", "tan", "√"],
    ["log", "ln", "(", ")", "^", "%"]
]

# Digits & operators
normal_buttons = [
    ["7", "8", "9", "/", "C"],
    ["4", "5", "6", "*", "-"],
    ["1", "2", "3", "+", "="],
    ["0", ".", "00"]
]

# Place scientific buttons
for i, row in enumerate(scientific_buttons, 1):
    for j, btn_text in enumerate(row):
        if btn_text == "x!":
            btn = Button(root, text=btn_text, font=("Segoe UI", 16), fg="white", bg="#444444",
                         command=lambda: disp.insert(END, "math.factorial("))
        else:
            btn = Button(root, text=btn_text, font=("Segoe UI", 16), fg="white", bg="#444444",
                         command=lambda b=btn_text: btn_click(b))
        btn.grid(row=i, column=j, sticky="nsew", padx=2, pady=2)

# Place normal buttons
start_row = len(scientific_buttons) + 1
for i, row in enumerate(normal_buttons):
    for j, btn_text in enumerate(row):
        if btn_text == "C":
            btn = Button(root, text=btn_text, font=("Segoe UI", 16), fg="white", bg="red",
                         command=clear_disp)
        elif btn_text == "=":
            btn = Button(root, text=btn_text, font=("Segoe UI", 16), fg="white", bg="green",
                         command=evaluate)
        else:
            btn = Button(root, text=btn_text, font=("Segoe UI", 16), fg="white", bg="#333333",
                         command=lambda b=btn_text: btn_click(b))
        btn.grid(row=start_row + i, column=j, sticky="nsew", padx=2, pady=2)

# Configure grid weight for resizing
for i in range(10):
    root.grid_rowconfigure(i, weight=1)
for j in range(6):
    root.grid_columnconfigure(j, weight=1)

root.mainloop()