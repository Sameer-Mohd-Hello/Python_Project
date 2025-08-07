import tkinter as tk
import random

# Initialize main window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x350")
root.config(bg="white")

choices = ["Rock", "Paper", "Scissors"]


def play(user_choice):
    computer_choice = random.choice(choices)
    result_label.config(text=f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors")
        or (user_choice == "Paper" and computer_choice == "Rock")
        or (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You win!"
    else:
        result = "You lose!"

    outcome_label.config(text=result)


def reset():
    result_label.config(text="Computer chose: ?")
    outcome_label.config(text="")


# Title label
tk.Label(root, text="Rock Paper Scissors", font=("Arial", 18, "bold"), bg="white").pack(
    pady=10
)

# Buttons
frame = tk.Frame(root, bg="white")
frame.pack(pady=10)

rock_btn = tk.Button(frame, text="Rock", width=10, command=lambda: play("Rock"))
paper_btn = tk.Button(frame, text="Paper", width=10, command=lambda: play("Paper"))
scissors_btn = tk.Button(
    frame, text="Scissors", width=10, command=lambda: play("Scissors")
)

rock_btn.grid(row=0, column=0, padx=5)
paper_btn.grid(row=0, column=1, padx=5)
scissors_btn.grid(row=0, column=2, padx=5)

# Result display
result_label = tk.Label(root, text="Computer chose: ?", font=("Arial", 14), bg="white")
result_label.pack(pady=10)

outcome_label = tk.Label(root, text="", font=("Arial", 16, "bold"), bg="white")
outcome_label.pack(pady=10)

# Reset button
tk.Button(root, text="Play Again", command=reset, bg="yellow").pack(pady=10)

# Start GUI loop
root.mainloop()
