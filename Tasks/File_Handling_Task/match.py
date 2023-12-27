import random

# Teams
teams = ['csk', 'mi', 'rcb', 'gt']

# Start the match
print("Welcome to the cricket match!")

# Toss
choices = ['Head', 'Tail']
user_team = input("Choose your team (csk, mi, rcb, gt): ")
user_choice = input("Enter your choice (Head/Tail): ")
toss_result = random.choice(choices)

print(f"TOSS: {toss_result}")

if user_choice.lower() == toss_result.lower():
    print("You won the toss!")
    current_team = user_team
else:
    print(f"{user_team} lost the toss!")
    teams.remove(user_team)
    current_team = random.choice(teams)

print(f"{current_team} will bat first!")

# Play the match for one over
print(f"\n{current_team} is batting:")
for ball in range(6):
    input("Enter to bowl...")  # For simplicity, just press Enter to bowl
    outcome = random.choice(['1', '2', '4', '6', '0', 'wicket', 'no ball', 'wide'])
    print(f"{current_team}: {outcome}")

    if outcome.isdigit():
        runs = int(outcome)
    else:
        runs = 0

    print(f"{current_team}: {runs} runs  ({ball + 1} ball)")

    if outcome.lower() == 'wicket':
        print("WICKET!")
        break






















































# import random

# class CricketMatch:
#     def __init__(self, team1, team2):
#         self.team1 = team1
#         self.team2 = team2
#         self.current_team = None
#         self.current_over = 0
#         self.current_ball = 0
#         self.runs = 0
#         self.wickets = 0

#     def start_match(self):
#         print(f"Welcome to the cricket match between {self.team1} and {self.team2}!")

#     def toss(self):
#         choices = ['Head', 'Tail']
#         user_choice = input("Enter your choice (Head/Tail): ")
#         toss_result = random.choice(choices)

#         print(f"TOSS: {toss_result}")

#         if user_choice.lower() == toss_result.lower():
#             print("You won the toss!")
#             self.current_team = self.team1
#         else:
#             print(f"{self.team2} won the toss!")
#             self.current_team = self.team2

#     def choose_to_bat_or_bowl(self):
#         choice = input("Choose Bat or Ball first: ")
#         if choice.lower() == 'bat':
#             print(f"{self.current_team} chose to bat first!")
#         else:
#             print(f"{self.current_team} chose to bowl first!")

#     def play_match(self):
#         print(f"\n{self.current_team} is batting:")
#         while self.current_over < 2:  # Let's assume a T20 match with 2 overs per team
#             self.play_over()
#             self.current_over += 1

#     def play_over(self):
#         for ball in range(6):
#             input("Enter to bowl...")  # For simplicity, just press Enter to bowl
#             outcome = random.choice(['1', '2', '4', '6', '0', 'wicket', 'no ball', 'wide'])
#             print(f"{self.current_team}: {outcome}")

#             if outcome.isdigit():
#                 self.runs += int(outcome)
#             elif outcome.lower() == 'wicket':
#                 self.wickets += 1

#             print(f"{self.current_team}: {self.runs}/{self.wickets}  ({self.current_over}.{ball + 1})")

#             if outcome.lower() == 'wicket':
#                 print("WICKET!")
#                 break

# if __name__ == "__main__":
#     team1 = input("Enter your team: ")
#     team2 = input("Opponent team: ")

#     match = CricketMatch(team1, team2)
#     match.start_match()
#     match.toss()
#     match.choose_to_bat_or_bowl()
#     match.play_match()
