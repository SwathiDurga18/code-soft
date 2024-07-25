import tkinter as tk
import random
from tkinter import messagebox

# Function to determine the winner of a round
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!", 0, 0
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        return "You win!", 1, 0
    else:
        return "Computer wins!", 0, 1

# Function to update the score labels
def update_scores(user_score, computer_score):
    user_score_label.config(text=f"Your Score: {user_score}")
    computer_score_label.config(text=f"Computer Score: {computer_score}")

# Function to play a round
def play_round():
    user_choice = user_choice_var.get()
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    result, user_score, computer_score = determine_winner(user_choice, computer_choice)

    # Update the result label and scores
    result_label.config(text=f"Computer chose {computer_choice}\n{result}")
    user_score_var.set(user_score_var.get() + user_score)
    computer_score_var.set(computer_score_var.get() + computer_score)
    update_scores(user_score_var.get(), computer_score_var.get())  # Update scores

    # Ask if the user wants to play another round using a custom dialog
    play_again = messagebox.askyesno("Play Again", "Do you want to play another round?")
    if not play_again:
        play_button.config(state=tk.DISABLED)  # Disable play button if the user doesn't want to play
        reset_button.config(state=tk.NORMAL)   # Enable reset button

# Function to reset the game
def reset_game():
    result_label.config(text="")
    user_choice_var.set("")
    user_score_var.set(0)
    computer_score_var.set(0)
    update_scores(0, 0)  # Reset score labels
    play_button.config(state=tk.NORMAL)   # Enable play button
    reset_button.config(state=tk.DISABLED)  # Disable reset button

# Create the main window
window = tk.Tk()
window.title("Rock, Paper, Scissors Game")
window.geometry("2000x2000")
# Create labels, buttons, and score labels
instructions_label = tk.Label(window, text="Choose rock, paper, or scissors:")
instructions_label.pack(pady=10)

user_choice_var = tk.StringVar()
user_choice_var.set("")  # Initial value

rock_button = tk.Radiobutton(window, text="Rock", variable=user_choice_var, value="rock")
paper_button = tk.Radiobutton(window, text="Paper", variable=user_choice_var, value="paper")
scissors_button = tk.Radiobutton(window, text="Scissors", variable=user_choice_var, value="scissors")

rock_button.pack()
paper_button.pack()
scissors_button.pack()

play_button = tk.Button(window, text="Play", command=play_round)
play_button.pack(pady=10)

result_label = tk.Label(window, text="", font=("Helvetica", 12))
result_label.pack()

user_score_var = tk.IntVar()
computer_score_var = tk.IntVar()

user_score_label = tk.Label(window, text="Your Score: 0", font=("Helvetica", 12))
computer_score_label = tk.Label(window, text="Computer Score: 0", font=("Helvetica", 12))

user_score_label.pack()
computer_score_label.pack()

reset_button = tk.Button(window, text="Reset", command=reset_game, state=tk.DISABLED)
reset_button.pack(pady=10)

# Customize the appearance to make it more game-like
window.configure(bg="lightblue")  # Background color
instructions_label.config(font=("Arial", 16), bg="lightblue")
rock_button.config(font=("Arial", 14), bg="lightblue")
paper_button.config(font=("Arial", 14), bg="lightblue")
scissors_button.config(font=("Arial", 14), bg="lightblue")
play_button.config(font=("Arial", 14), bg="green", fg="white")
reset_button.config(font=("Arial", 14), bg="pink", fg="white")

# Run the GUI
window.mainloop()
