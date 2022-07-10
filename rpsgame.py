import random

while True:

    choices = ["rock","paper", "scissors"]

    computer = random.choice(choices)

    player = input("rock, paper or scissors? ")

    while player not in choices:
        player = input("rock, paper, scissors? ").lower()

    win = "YOU WIN"

    lose = "YOU LOSE"
    #status of both player and computer
    input("Computer says... (Press enter to continue)")
    print(computer + "!")
        
    #draw statement
    if player == computer:
        print("I's a draw NOOB")

    #win and lose condition with rock
    elif player == "rock":
        if computer == "scissors":
            print(win)
        elif computer == "paper":
            print(lose)

    #win and lose condition with paper
    elif player == "paper":
        if computer == "rock":
            print(win)
        elif computer == "scissors":
            print(lose)

    #win and lose condition with scissors
    elif player == "scissors":
        if computer == "paper":
            print(win)
        elif computer == "rock":
            print(lose)

    playAgain = input("Play again? (yes/no) ").lower()
    if playAgain != "yes":
        break 
print("Bye!")