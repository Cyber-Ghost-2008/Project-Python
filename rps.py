import random

choices = ["Rock", "Paper", "Scissor"]

while True:
    computer_choice = random.choice(choices)
    usr_input = input("Rock or Paper or Scissor? ")
    if usr_input not in choices:
        print(f'Invalid Input... Please select only Rock, Paper, or Scissor')
        continue

    if computer_choice == "Rock" and usr_input == "Paper":
        print(f"You Won! My choice is {computer_choice} & Your choice is {usr_input}")
    elif computer_choice == "Rock" and usr_input == "Scissor":
        print(f"You Lost! My choice is {computer_choice} & Your choice is {usr_input}")
    elif computer_choice == "Paper" and usr_input == "Rock":
        print(f"You Lost! My choice is {computer_choice} & Your choice is {usr_input}")
    elif computer_choice == "Paper" and usr_input == "Scissor":
        print(f"You Won! My choice is {computer_choice} & Your choice is {usr_input}")
    elif computer_choice == "Scissor" and usr_input == "Rock":
        print(f"You Won! My choice is {computer_choice} & Your choice is {usr_input}")
    elif computer_choice == "Scissor" and usr_input == "Paper":
        print(f"You Lost! My choice is {computer_choice} & Your choice is {usr_input}")
    else:
        print(f"TIE!... My choice is {computer_choice} & Your choice is {usr_input}")
        break