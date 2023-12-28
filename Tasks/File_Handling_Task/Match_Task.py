import random

# ============== Batting bowling Function ============
def batting_bowling(decision, team_1, team_2):
    if decision.lower() == "bat":
        print(f"{team_1} is Batting!")
        score = 0
        ball = 0
        while ball < 6:
            input("Press Enter to bowl...")
            action = random.choice([1, 2, 4, 6, 0, "wicket", "no ball", "wide"])
            if action == "wicket":
                print(f"Oops! {team_1} lost a wicket.")
            elif action == "no ball":
                score += 1
                print(f"No ball! {team_1} gets 1 run.")
            elif action == "wide":
                score += 1
                print(f"Wide ball! {team_1} gets 1 run.")
            else:
                score += action
                print(f"{team_1} scores {action} runs in this ball. Total: {score}")
            ball += 1

        print(f"\n{team_1} scored {score} runs!")
        return score

    elif decision.lower() == "ball":
        print(f"{team_2}' bowling!")
        batting_score = batting_bowling("bat", team_2, team_1)
        print(f"{team_1} scored {batting_score}/{random.randint(1, 6)} in 1 over.")
        print(f"{team_2} needs {batting_score + 1} runs to win.")
        return batting_score

# ================== Code Starts Here

print("===============  Anjali Mam's IPL ===============")

teams = ["CSK", "GT", "RCB", "MI"]
print("1) CSK")
print("2) GT")
print("3) RCB")
print("4) MI")

your_team = input("Enter Your Team: ").upper()
teams.remove(your_team)
opp_team = random.choice(teams)

print(f"=================== {your_team} vs {opp_team} ===================")

# ====================== toss time
print("TOSS TIME:")
toss_result = random.choice(["HEAD", "TAIL"])
while True:
    your_choice = input("Enter your choice (Head/Tail): ").upper()
    if your_choice == "HEAD" or your_choice == "TAIL":
        print(f"TOSS RESULT: It's {toss_result}")
        break
    else:
        print("Please Enter Valid Input (Head or Tail)")

# ====================== Batting bowling Time
you_bat_ball = ""

if your_choice == toss_result:
    print("You won the toss!")
    while True:
        you_bat_ball = input("Choose Bat or Ball first: ").lower()
        if you_bat_ball in ["bat", "ball"]:
            break
        else:
            print("Please Enter Valid Input (bat/ball)")

    if you_bat_ball == "bat":
        your_score = batting_bowling("bat", your_team, opp_team)
        input("Press Enter to continue to the second inning...")
        opp_score = batting_bowling("bat", opp_team, your_team)
    elif you_bat_ball == "ball":
        opp_score = batting_bowling("ball", your_team, opp_team)
        your_score = batting_bowling("bat", opp_team, your_team)

else:
    opp_bat_ball = random.choice(["bat", "ball"])
    print(f"You lost the toss. {opp_team} won the toss and chose to {opp_bat_ball}.")
    if opp_bat_ball == "bat":
        opp_score = batting_bowling("bat", opp_team, your_team)
        input("Press Enter to continue to the second inning...")
        your_score = batting_bowling("bat", your_team, opp_team)
    elif opp_bat_ball == "ball":
        your_score = batting_bowling("ball", your_team, opp_team)
        opp_score = batting_bowling("bat", opp_team, your_team)

if your_score > opp_score:
    print(f"{your_team} Won The Match")
elif your_score < opp_score:
    print(f"{your_team} Lost The Match")
else:
    print("It's a Tie!")
