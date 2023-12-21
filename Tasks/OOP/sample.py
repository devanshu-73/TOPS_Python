import tkinter
import random

# Global Variables to store score
user_score = 0
machine_score = 0

# Function to play game
def game(player):
    global user_score, machine_score

    # List Of Choice for The Computer
    choices = ["ROCK", "PAPER", "SCISSOR"]

    # declaration
    # [.random na help computer ani choices lase ane try karse k let he wins ]
    computer_choice = random.choice(choices)

    # Winner Determine
    # attyare result name na variable ma winner decission store thase ane pache winnerdeciddion namme nu function banavsu  jem playerc ane computer/machine no statements passs karisu
    result = winnerDecission(player, computer_choice)

    # Label Updating with choice and result
    user_choice_label["text"] = f"Your Choice: {player}"
    computer_choice_label["text"] = f"Computer's Choice: {computer_choice}"
    result_label["text"] = f"Result: {result}"

    # Updating Score based on te result
    if result == "GREAT! You Win":
        user_score += 1
    elif result == "Computer Win":
        machine_score += 1

    # Updating score Labels
    user_score_label["text"] = f"User: {user_score}"
    machine_score_label["text"] = f"Computer: {machine_score}"
    result_score_label["text"] = f"Result: {user_score} - {machine_score}"

# Function to determine Winner
def winnerDecission(player, computer_choice):
    if player == computer_choice:  # Agar player ane computer no score sarkho hase to niche nu return statemnets pass thase
        return "OOPS It's a Tie"
    # pachi user ne jitava mate ni condition check thase jose agar baddhu oppsite hoi computer thi to player jitse
    elif ((player == "ROCK" and computer_choice == "SCISSOR") or
          (player == "PAPER" and computer_choice == "ROCK") or
          (player == "SCISSOR" and computer_choice == "PAPER")):
        return "GREAT! You Win"
    else:
        return "Computer Win"

# CREATING THE SCREEN OF TKINTER WINDOW AND ITS LAYOUT BUTTONS , TEXT , LABELS
screen = tkinter.Tk()  # ani madad thi gui banse
screen.title("WELCOME TO THE GAME OF ROCK PAPER AND SCISSOR")  # je screen pop up thasse ne ani top ma title banse aa nam nu
screen.geometry("550x550")  # ana thi  poped screen ni hheight width set thse
# "GAME TITLE LABEL"
label = tkinter.Label(screen, text="ROCK PAPER SCISSOR GAME ", font=("Arial", 25, "bold"))
label.place(x=85, y=45)

# ROCK BUTOON STYLING
rock_button = tkinter.Button(screen, command=lambda: game("ROCK"), text="Rock", bg="black", fg="white",
                             font=("Arial", 15, "bold"), height=4, width=5)
rock_button.place(x=150, y=100)

# PAPER BUTTON STYLING
paper_button = tkinter.Button(screen, command=lambda: game("PAPER"), text="Paper", bg="black", fg="white",
                              font=("Arial", 15, "bold"), height=4, width=5)
paper_button.place(x=250, y=100)

# SCISSOR BUTTON STYLING
scissor_button = tkinter.Button(screen, command=lambda: game("SCISSOR"), text="Scissor", bg="black", fg="white",
                                font=("Arial", 15, "bold"), height=4, width=5)
scissor_button.place(x=350, y=100)

# LABELS FOR DISPLAYING CHOICE AND RESULT
user_choice_label = tkinter.Label(screen, text="Your choice: ", font=("Arial", 14, "bold"))
user_choice_label.place(x=50, y=200)

computer_choice_label = tkinter.Label(screen, text="Computer's choice: ", font=("Arial", 14, "bold"))
computer_choice_label.place(x=50, y=230)

result_label = tkinter.Label(screen, text="Result: ", font=("Arial", 14, "bold"))
result_label.place(x=50, y=260)

# DISPLAYING SCORES
user_score_label = tkinter.Label(screen, text=f"User: {user_score}", font=("Arial", 14, "bold"))
user_score_label.place(x=400, y=200)

machine_score_label = tkinter.Label(screen, text=f"Computer: {machine_score}", font=("Arial", 14, "bold"))
machine_score_label.place(x=400, y=230)

result_score_label = tkinter.Label(screen, text=f"Result: {user_score} - {machine_score}", font=("Arial", 14, "bold"))
result_score_label.place(x=400, y=260)

screen.mainloop()
