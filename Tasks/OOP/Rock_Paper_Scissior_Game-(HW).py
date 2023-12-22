import tkinter
import random

user_score = 0
computer_score = 0

def play_game(player_choice):
    global user_score = 0 computer_score
    l1 = ["Paper", "Rock", "Scissors"] 
    computer_choice = random.choice(l1)
    result = winner_decision(player_choice, computer_choice)

    user_choice_label["text"] = f"Your choice: {player_choice}"
    computer_choice_label["text"] = f"Computer's choice: {computer_choice}"
    result_label["text"] = f"Result: {result}"

    if result == "You win!":
        user_score += 1
    elif result == "Computer wins!":
        computer_score += 1

    user_point["text"] = f"User: {user_score}"
    computer_point["text"] = f"Computer: {computer_score}"
    result_score["text"] = f"Result: {user_score} - {computer_score}"

def winner_decision(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif ((player_choice == "Rock" and computer_choice == "Scissors") or
         (player_choice == "Paper" and computer_choice == "Rock") or 
         (player_choice == "Scissors" and computer_choice == "Paper")):
        return "You win!"
    else:
        return "Computer wins!"

screen = tkinter.Tk()
screen.title("Rock, Paper, Scissors Game")
screen.geometry("550x550")

label = tkinter.Label(screen, text="Rock Paper Scissors Game", font=("Arial", 20, "bold"))
label.place(x=95, y=50)

rock_button = tkinter.Button(screen, command=lambda: play_game("Rock"), text="Rock", bg="black", fg="white", font=("Arial", 14, "bold"), height=2, width=8)
rock_button.place(x=120, y=100)

paper_button = tkinter.Button(screen, command=lambda: play_game("Paper"), text="Paper", bg="black", fg="white", font=("Arial", 14, "bold"), height=2, width=8)
paper_button.place(x=240, y=100)

scissors_button = tkinter.Button(screen, command=lambda: play_game("Scissors"), text="Scissors", bg="black", fg="white", font=("Arial", 14, "bold"), height=2, width=8)
scissors_button.place(x=360, y=100)

user_choice_label = tkinter.Label(screen, text="Your choice: ", font=("Arial", 14, "bold"))
user_choice_label.place(x=50, y=200)

computer_choice_label = tkinter.Label(screen, text="Computer's choice: ", font=("Arial", 14, "bold"))
computer_choice_label.place(x=50, y=230)

result_label = tkinter.Label(screen, text="Result: ", font=("Arial", 14, "bold"))
result_label.place(x=50, y=260)

user_point = tkinter.Label(screen, text=f"User: {user_score}", font=("Arial", 14, "bold"))
user_point.place(x=400, y=200)

computer_point = tkinter.Label(screen, text=f"Computer: {computer_score}", font=("Arial", 14, "bold"))
computer_point.place(x=400, y=230)

result_score = tkinter.Label(screen, text=f"Result: {user_score} - {computer_score}", font=("Arial", 14, "bold"))
result_score.place(x=400, y=260)

# Run the Tkinter event loop
screen.mainloop()
