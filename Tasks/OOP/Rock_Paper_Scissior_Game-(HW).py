import tkinter
import random

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        return "You win!"
    else:
        return "Computer wins!"

def play_game(player_choice):
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    result = determine_winner(player_choice, computer_choice)
    
    result_label.config(text=f"Computer chose {computer_choice}. {result}")

screen = tkinter.Tk()  # Create Screen
screen.title("Rock, Paper, Scissors Game")
screen.geometry("400x400")

label = tkinter.Label(screen, text="Choose Rock, Paper, or Scissors:")
label.place(x=130, y=50)  # Adjusted the position

rock_button = tkinter.Button(screen, text="Rock", command=lambda: play_game("Rock"), height=3, width=10)
rock_button.place(x=50, y=100)

paper_button = tkinter.Button(screen, text="Paper", command=lambda: play_game("Paper"), height=3, width=10)
paper_button.place(x=150, y=100)

scissors_button = tkinter.Button(screen, text="Scissors", command=lambda: play_game("Scissors"), height=3, width=10)
scissors_button.place(x=250, y=100)

result_label = tkinter.Label(screen, text="")
result_label.place(x=200, y=250)  # Adjusted the position

# Run the Tkinter event loop
screen.mainloop()
