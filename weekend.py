import random

rules = {
        "Rock": "Scissors",
        "Paper": "Rock",
        "Scissors": "Paper"
    }


win_score, lose_score, draw = 0, 0, 0

while True:
    user = input("Enter one of Rock/Paper/Scissors").capitalize() # Get user input
    if user == ("Quit"):
        break
    cpu = random.choice(["Rock", "Paper", "Scissors"]) # Get computer input
    print(f"I choose {user}")
    print(f"cpu chooses {cpu}") 
# letting you know this is how it determines who wins
    
#     if user == ("Rock"):
#         if cpu == ("Rock"):
#             print("It's a tie!")
#         elif cpu == ("Paper"):
#             print("You lose!")
#         else:
#             print("You win!")
#     if user == ("Paper"):
#         if cpu == ("Rock"):
#             print("You win!")
#         elif cpu == ("Paper"):
#             print("It's a tie!")
#         else:
#             print("You lose!")
#     if user == ("Scissors"):
#         if cpu == ("Scissors"):
#             print("It's a tie!")
#         elif cpu == ("Paper"):
#             print("You win!")
#         else:
#             print("You lose!")
    if user == cpu:
        print("It's a tie!")
        draw += 1
    elif rules[user] == cpu:
        print("You won!")
        win_score += 1
    else:
        print("You lose!")
        lose_score += 1
    print(f"You have {win_score} Cpu has {lose_score} Ties {draw}")

