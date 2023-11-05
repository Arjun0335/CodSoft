import tkinter as tk
import random

# Function to determine the game result
def play_rps(player_choice):
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)

    if player_choice == computer_choice:
        result_label.config(text=f"It's a tie! Computer chose {computer_choice}")
    elif (
        (player_choice == "Rock" and computer_choice == "Scissors")
        or (player_choice == "Paper" and computer_choice == "Rock")
        or (player_choice == "Scissors" and computer_choice == "Paper")
    ):
        result_label.config(text=f"You win! Computer chose {computer_choice}")
    else:
        result_label.config(text=f"You lose! Computer chose {computer_choice}")

# Create the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")

# Create labels and buttons for the game
label = tk.Label(root, text="Choose Rock, Paper, or Scissors:")
label.pack(pady=10)

rock_button = tk.Button(root, text="Rock", command=lambda: play_rps("Rock"))
rock_button.pack()

paper_button = tk.Button(root, text="Paper", command=lambda: play_rps("Paper"))
paper_button.pack()

scissors_button = tk.Button(root, text="Scissors", command=lambda: play_rps("Scissors"))
scissors_button.pack()

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
