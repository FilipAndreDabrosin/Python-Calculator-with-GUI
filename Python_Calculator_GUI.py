import tkinter as tk
import re


calculation = ""

def evaluate_expression(expression):
    try:

        operators = {'+': (1, lambda x, y: x + y), '-': (1, lambda x, y: x - y),
                     '*': (2, lambda x, y: x * y), '/': (2, lambda x, y: x / y)}

        def shunting_yard(expression):
            output = []
            operators_stack = []

            for token in re.findall(r'\d+|\+|\-|\*|\/|\(|\)', expression):
                if token.isdigit():
                    output.append(token)
                elif token == '(':
                    operators_stack.append(token)
                elif token == ')':
                    while operators_stack and operators_stack[-1] != '(':
                        output.append(operators_stack.pop())
                    operators_stack.pop()
                else:
                    while operators_stack and operators_stack[-1] in operators and operators[token][0] <= operators[operators_stack[-1]][0]:
                        output.append(operators_stack.pop())
                    operators_stack.append(token)

            while operators_stack:
                output.append(operators_stack.pop())

            return output

        def calculate_rpn(rpn):
            stack = []
            for token in rpn:
                if token.isdigit():
                    stack.append(float(token))
                elif token in operators:
                    y, x = stack.pop(), stack.pop()
                    stack.append(operators[token][1](x, y))
            return stack[0]

        rpn = shunting_yard(expression)
        print("Reverse Polish Notation:", rpn)
        result = calculate_rpn(rpn)
        print("Calculated Result:", result)
        return str(result)
    except Exception as e:
        print("Error:", e)
        return "Error"
    
def on_click(button_text):
    global calculation
    current_text = entry_var.get()
    
    if button_text == '=':
        print("Calculation:", calculation)
        result = evaluate_expression(calculation)
        print("Result:", result)
        entry_var.set(result)
    elif button_text == 'C':
        calculation = ""
        entry_var.set('')
    else:
        calculation += button_text
        entry_var.set(current_text + button_text)


def on_enter(event):
    event.widget.config(bg="#2c2c4c")

def on_leave(event):
    event.widget.config(bg="#0e0e24")



root = tk.Tk()
root.geometry("300x275")
root.title("Calculator")
root.configure(bg="#020f12")
icon = tk.PhotoImage(file="calculator_icon.png")
button_pressed = tk.BooleanVar
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, justify='right', font=('Arial', 16), bd=10, bg="#2c2c4c", fg="light blue")
entry.grid(row=0, column=1, columnspan=4)
    
class Btn:          
    def __init__(self, root, text, command, row, column):
        self.button = tk.Button(root, text=text, command=command, width=5, font=("Arial, 14"), bg="#0e0e24", fg="light blue")
        self.button.grid(row=row, column=column)
        self.button.bind("<Enter>", on_enter)
        self.button.bind("<Leave>", on_leave)



btn_1 = tk.Button(root, text="1", command=lambda: on_click("1"), width=5, font=("Arial, 14"), bg="#0e0e24", fg="light blue", padx=5, pady=5, bd=0)
btn_1.grid(row=2, column=1)
btn_2 = tk.Button(root, text="2", command=lambda: on_click("2"),width=5, font=("Arial, 14"), bg="#0e0e24", fg="light blue", padx=5, pady=5, bd=0)
btn_2.grid(row=2, column=2)
btn_3 = tk.Button(root, text="3", command=lambda: on_click("3"), width=5, font=("Arial, 14"), bg="#0e0e24", fg="light blue", padx=5, pady=5, bd=0 )
btn_3.grid(row=2, column=3)
btn_4 = tk.Button(root, text="4", command=lambda: on_click("4"), width=5, font=("Arial, 14"), bg="#0e0e24", fg="light blue", padx=5, pady=5, bd=0)
btn_4.grid(row=3, column=1)
btn_5 = tk.Button(root, text="5", command=lambda: on_click("5"), width=5, font=("Arial, 14"), bg="#0e0e24", fg="light blue", padx=5, pady=5, bd=0)
btn_5.grid(row=3, column=2)
btn_6 = tk.Button(root, text="6", command=lambda: on_click("6"), width=5, font=("Arial, 14"), bg="#0e0e24", fg="light blue", padx=5, pady=5, bd=0)
btn_6.grid(row=3, column=3)
btn_7 = tk.Button(root, text="7", command=lambda: on_click("7"), width=5, font=("Arial, 14"), bg="#0e0e24", fg="light blue", padx=5, pady=5, bd=0)
btn_7.grid(row=4, column=1)
btn_8 = tk.Button(root, text="8", command=lambda: on_click("8"), width=5, font=("Arial, 14"), bg="#0e0e24", fg="light blue", padx=5, pady=5, bd=0)
btn_8.grid(row=4, column=2)
btn_9 = tk.Button(root, text="9", command=lambda: on_click("9"), width=5, font=("Arial, 14"), bg="#0e0e24", fg="light blue", padx=5, pady=5, bd=0)
btn_9.grid(row=4, column=3)
btn_0 = tk.Button(root, text="0", command=lambda: on_click("0"), width=5, font=("Arial, 14"), bg="#0e0e24", fg="light blue", padx=5, pady=5, bd=0)
btn_0.grid(row=5, column=2)
btn_plus = tk.Button(root, text="+", command=lambda: on_click("+"), width=5, font=("Arial, 14"), bg="#0e0e24", fg="light blue", padx=5, pady=5, bd=0)
btn_plus.grid(row=2, column=4)
btn_minus = tk.Button(root, text="-", command=lambda: on_click("-"), width=5, font=("Arial, 14"), bg="#0e0e24", fg="light blue", padx=5, pady=5, bd=0)
btn_minus.grid(row=3, column=4)
btn_multiplication = tk.Button(root, text="x", command=lambda: on_click("*"), width=5, font=("Arial, 14"), bg="#0e0e24", fg="light blue", padx=5, pady=5, bd=0)
btn_multiplication.grid(row=4, column=4)
btn_dividing = tk.Button(root, text="÷", command=lambda: on_click("/"), width=5, font=("Arial, 14"), bg="#0e0e24", fg="light blue", padx=5, pady=5, bd=0)
btn_dividing.grid(row=5, column=4)
btn_open = tk.Button(root, text="(", command=lambda: on_click("("), width=5, font=("Arial, 14"), bg="#0e0e24", fg="light blue", padx=5, pady=5, bd=0)
btn_open.grid(row=5, column=1)
btn_close= tk.Button(root, text=")", command=lambda: on_click(")"), width=5, font=("Arial, 14"), bg="#0e0e24", fg="light blue", padx=5, pady=5, bd=0)
btn_close.grid(row=5, column=3)
btn_equals = tk.Button(root, text="=", command=lambda: on_click("="), width=11, font=("Arial, 14"), bg="#0e0e24", fg="light blue", padx=10, pady=5, bd=0)
btn_equals.grid(row=6, column=3, columnspan=2)
btn_clear = tk.Button(root, text="C", command=lambda:  on_click("C"), width=11, font=("Arial, 14"), bg="#0e0e24", fg="light blue", padx=10, pady=5, bd=0)
btn_clear.grid(row=6, column=1, columnspan=2)

btn_1.bind("<Enter>", on_enter)
btn_1.bind("<Leave>", on_leave)
btn_2.bind("<Enter>", on_enter)
btn_2.bind("<Leave>", on_leave)
btn_3.bind("<Enter>", on_enter)
btn_3.bind("<Leave>", on_leave)
btn_4.bind("<Enter>", on_enter)
btn_4.bind("<Leave>", on_leave)
btn_5.bind("<Enter>", on_enter)
btn_5.bind("<Leave>", on_leave)
btn_6.bind("<Enter>", on_enter)
btn_6.bind("<Leave>", on_leave)
btn_7.bind("<Enter>", on_enter)
btn_7.bind("<Leave>", on_leave)
btn_8.bind("<Enter>", on_enter)
btn_8.bind("<Leave>", on_leave)
btn_9.bind("<Enter>", on_enter)
btn_9.bind("<Leave>", on_leave)
btn_0.bind("<Enter>", on_enter)
btn_0.bind("<Leave>", on_leave)
btn_close.bind("<Enter>", on_enter)
btn_close.bind("<Leave>", on_leave)
btn_open.bind("<Enter>", on_enter)
btn_open.bind("<Leave>", on_leave)
btn_equals.bind("<Enter>", on_enter)
btn_equals.bind("<Leave>", on_leave)
btn_clear.bind("<Enter>", on_enter)
btn_clear.bind("<Leave>", on_leave)

root.mainloop()
