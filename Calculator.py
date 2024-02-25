import tkinter as tk

def button_click(symbol):
    current = display.get()
    if current == "Error":
        current = ""
    if symbol == "=":
        try:
            result = str(eval(current))
            display.delete(0, tk.END)
            display.insert(tk.END, result)
        except:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
    elif symbol == "C":
        display.delete(0, tk.END)
    else:
        display.insert(tk.END, symbol)

root = tk.Tk()
root.title("Simple Calculator")

display = tk.Entry(root, width=20, font=("Arial", 16))
display.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C'
]

row = 1
col = 0
for button in buttons:
    tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 14), command=lambda b=button: button_click(b)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()