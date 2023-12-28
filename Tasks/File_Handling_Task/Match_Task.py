import random

def batting_bowling(team, opponent, decision):
    if decision == "bat":
        print(f"{team}'s {decision}ing!")
        print(f"{opponent}'s {'Bowling' if decision == 'bat' else 'Bating'}!")
    elif decision == "bowl":
        print(f"{opponent}'s {decision}ing!")
        print(f"{team}'s {'Bowling' if decision == 'bat' else 'Bating'}!")
     
    score = 0
    for ball in range(6):
        input(f"Press Enter to bowl for {team}...")
        action = random.choice([1, 2, 4, 6, 0, "wicket", "no ball", "wide"])

        if action == "wicket":
            print(f"Oops! {team} {'lost' if decision == 'bat' else 'took'} a wicket.")
        elif action == "no ball" or action == "wide":
            runs = 1
            if action == "wide":
                print(f"Wide ball! {team} gets 1 run.")
            else:
                print(f"No ball! {team} gets 1 run.")
            score += runs
        else:
            runs = action
            score += runs
            action_type = 'scores' if decision == 'bat' else 'gets'
            print(f"{team} {action_type} {runs} runs in this ball. Total: {score}")

    return score

print("===============  Anjali Mam's IPL ===============")

teams = ["CSK", "GT", "RCB", "MI"]
print("1) CSK\n2) GT\n3) RCB\n4) MI")
your_team = input("Enter Your Team: ").upper()
teams.remove(your_team)
opp_team = random.choice(teams)

print(f"=================== {your_team} vs {opp_team} ===================")

toss_result = random.choice(["HEAD", "TAIL"])
your_choice = input("Enter your choice (Head/Tail): ").upper()
if your_choice in ["HEAD", "TAIL"]:
    print(f"TOSS RESULT: It's {toss_result}")
else:
    print("Please Enter Valid Input (Head or Tail)")

you_bat_bowl = ""
if your_choice == toss_result:
    print("You won the toss!")
    you_bat_bowl = input("Choose Bat or Bowl first: ").lower()
    while you_bat_bowl not in ["bat", "bowl"]:
        print("Please Enter Valid Input (bat/Bowl)")
        you_bat_bowl = input("Choose Bat or Bowl first: ").lower()
else:
    opp_bat_bowl = random.choice(["bat", "bowl"])
    print(f"You lost the toss. {opp_team} won the toss and chose to {opp_bat_bowl}.")
    you_bat_bowl = "bowl" if opp_bat_bowl == "bat" else "bat"

if you_bat_bowl == "bat":
    your_score = batting_bowling(your_team, opp_team, "bat")
    input("Press Enter to continue to the second inning...")
    opp_score = batting_bowling(opp_team, your_team, "bowl")
else:
    opp_score = batting_bowling(opp_team, your_team, "bat")
    input("Press Enter to continue to the second inning...")
    your_score = batting_bowling(your_team, opp_team, "bowl")

if your_score > opp_score:
    print(f"{your_team} Won The Match")
elif your_score < opp_score:
    print(f"{your_team} Lost The Match")
else:
    print("It's a Tie!")

# import random

# def perform_inning(team, opponent, decision):
#     if decision == "bat":
#         print(f"{team}'s {decision.capitalize()}ing!")
#         print(f"{opponent}'s {'Bowling' if decision == 'bat' else 'Batting'}!")
#     elif decision == "bowl":
#         print(f"{opponent}'s {decision.capitalize()}ing!")
#         print(f"{team}'s {'Bowling' if decision == 'bat' else 'Batting'}!")
     
#     score = 0
#     for ball in range(6):
#         input(f"Press Enter to bowl for {team}...")
#         action = random.choice([1, 2, 4, 6, 0, "wicket", "no ball", "wide"])

#         if action == "wicket":
#             print(f"Oops! {team} {'lost' if decision == 'bat' else 'took'} a wicket.")
#         elif action == "no ball" or action == "wide":
#             runs = 1
#             if action == "wide":
#                 print(f"Wide ball! {team} gets 1 run.")
#             else:
#                 print(f"No ball! {team} gets 1 run.")
#             score += runs
#         else:
#             runs = action
#             score += runs
#             print(f"{team} {'scores' if decision == 'bat' else 'concedes'} {runs} runs in this ball. Total: {score}")

#     print(f"\n{team} {'scored' if decision == 'bat' else 'gave away'} {score} runs!")
#     return score

# print("===============  Anjali Mam's IPL ===============")

# teams = ["CSK", "GT", "RCB", "MI"]
# print("1) CSK\n2) GT\n3) RCB\n4) MI")
# your_team = input("Enter Your Team: ").upper()
# teams.remove(your_team)
# opp_team = random.choice(teams)

# print(f"=================== {your_team} vs {opp_team} ===================")

# toss_result = random.choice(["HEAD", "TAIL"])
# your_choice = input("Enter your choice (Head/Tail): ").upper()
# if your_choice in ["HEAD", "TAIL"]:
#     print(f"TOSS RESULT: It's {toss_result}")
# else:
#     print("Please Enter Valid Input (Head or Tail)")

# you_bat_bowl = ""
# if your_choice == toss_result:
#     print("You won the toss!")
#     you_bat_bowl = input("Choose Bat or Bowl first: ").lower()
#     while you_bat_bowl not in ["bat", "bowl"]:
#         print("Please Enter Valid Input (bat/Bowl)")
#         you_bat_bowl = input("Choose Bat or Bowl first: ").lower()
# else:
#     opp_bat_bowl = random.choice(["bat", "bowl"])
#     print(f"You lost the toss. {opp_team} won the toss and chose to {opp_bat_bowl}.")
#     you_bat_bowl = "bowl" if opp_bat_bowl == "bat" else "bat"

# if you_bat_bowl == "bat":
#     your_score = perform_inning(your_team, opp_team, "bat")
#     input("Press Enter to continue to the second inning...")
#     opp_score = perform_inning(opp_team, your_team, "bowl")
# else:
#     opp_score = perform_inning(opp_team, your_team, "bat")
#     input("Press Enter to continue to the second inning...")
#     your_score = perform_inning(your_team, opp_team, "bowl")

# if your_score > opp_score:
#     print(f"{your_team} Won The Match")
# elif your_score < opp_score:
#     print(f"{your_team} Lost The Match")
# else:
#     print("It's a Tie!")
