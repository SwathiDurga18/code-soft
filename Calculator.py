import tkinter as tk

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operator_var.get()

        if operation == "+":
            result.set(num1 + num2)
        elif operation == "-":
            result.set(num1 - num2)
        elif operation == "*":
            result.set(num1 * num2)
        elif operation == "/":
            if num2 == 0:
                result.set("Cannot divide by zero")
            else:
                result.set(num1 / num2)
    except ValueError:
        result.set("Invalid input")

# Create the main window
window = tk.Tk()
window.title("Simple Calculator")

# Entry fields for numbers
entry1 = tk.Entry(window)
entry2 = tk.Entry(window)

entry1.grid(row=0, column=0, padx=10, pady=10)
entry2.grid(row=0, column=1, padx=10, pady=10)

# Label for the result
result = tk.StringVar()
result_label = tk.Label(window, textvariable=result)
result_label.grid(row=1, column=0, columnspan=2)

# Dropdown menu for operations
operator_var = tk.StringVar()
operator_choices = ["+", "-", "*", "/"]
operator_var.set("+")
operator_menu = tk.OptionMenu(window, operator_var, *operator_choices)
operator_menu.grid(row=0, column=2, padx=10, pady=10)

# Calculate button
calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.grid(row=1, column=2, padx=10, pady=10)

# Run the GUI
window.mainloop()
