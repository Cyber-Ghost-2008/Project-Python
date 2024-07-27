import random
import time
while True:
    choices = ["Rock", "Paper", "Scissor"]
    computer_choice1 = random.choice(choices)
    computer_choice2 = random.choice(choices)
    if computer_choice1 == "Rock" and computer_choice2 == "Paper":
        print(f"Computer 1 Won! Its choice is {computer_choice2} & 2nd Computer's choice is {computer_choice2}")
    elif computer_choice1 == "Rock" and computer_choice2 == "Scissor":
        print(f"Computer 1 Loss! Its choice is {computer_choice2} & 2nd Computer's choice is {computer_choice2}")
    elif computer_choice1 == "Paper" and computer_choice2 == "Rock":
        print(f"Computer 1 Loss! Its choice is {computer_choice2} & 2nd Computer's choice is {computer_choice2}")
    elif computer_choice1 == "Paper" and computer_choice2 == "Scissor":
        print(f"Computer 1 Won! Its choice is {computer_choice2} & 2nd Computer's choice is {computer_choice2}")
    elif computer_choice1 == "Scissor" and computer_choice2 == "Rock":
        print(f"Computer 1 Won! Its choice is {computer_choice2} & 2nd Computer's choice is {computer_choice2}")
    elif computer_choice1 == "Scissor" and computer_choice2 == "Paper":
        print(f"Computer 1 Loss! Its choice is {computer_choice2} & 2nd Computer's choice is {computer_choice2}")
    elif computer_choice1 ==  computer_choice2:
        print(f"Try Again... Its choice is {computer_choice2} & 2nd Computer's choice is {computer_choice2}")
    else:
        print(f'Invalid Input... Please select only Rock, Paper or Scissor')
    time.sleep(0.5)