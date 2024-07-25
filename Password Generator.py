import tkinter as tk
import random
import string


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_and_display_password():
    try:
        password_length = int(length_entry.get())

        if password_length <= 0:
            result_label.config(text="Password length must be a positive integer.")
        else:
            password = generate_password(password_length)
            result_label.config(text="Generated Password: " + password)
    except ValueError:
        result_label.config(text="Invalid input. Please enter a valid password length (a positive integer).")


window = tk.Tk()
window.title("Password Generator")
window.geometry("2000x2000")  
window.configure(bg="skyblue")  


length_label = tk.Label(window, text="Enter Password Length:", bg=window.cget("bg"), font=("Helvetica", 14))
length_label.pack(pady=20)

length_entry = tk.Entry(window, font=("Helvetica", 14))
length_entry.pack(pady=10, padx=50, ipady=10)


generate_button = tk.Button(window, text="Generate Password", command=generate_and_display_password,
                            bg="pink", font=("Helvetica", 12), relief=tk.RAISED)
generate_button.pack(pady=10)


result_label = tk.Label(window, text="", bg=window.cget("bg"), font=("Helvetica", 14))
result_label.pack()

length_entry.focus_set()
length_entry.selection_range(0, tk.END)

window.mainloop()
