import random
while True:
    print(" >>> r = rock , p = paper , s = scissors <<<")
    choices=["Rock" , "Paper" , "Scissors"]
    computer=random.choice(choices)
    choice=["r","p","s","R","S","P"]
    player = None

    while player not in choice:
        player = input('''enter your choice r , p , s >> ''').lower()
        if player == "r":
            print("yours  >>  Rock")
            print("computer >> " + computer)
        elif player == "s":
            print("yours  >> Scissors")
            print("computer >> " + computer)
        elif player == "p":
            print("yours >>  Paper")
            print("computer >> " + computer)
        if player == "r":
            if computer == "Paper":
                print(" You lose !! ")
            elif computer == "Rock":
                print("Its a tie !!")
            else:
                print(" You won !! ")
        elif player == "p":
            if computer == "Scissors":
                print(" You lose !! ")
            elif computer == "Paper":
                print("Its a tie !!")
            else:
                print(" You won !! ")
        elif player == "s":

            if computer == "Rock":
                print(" You lose !! ")
            elif computer == "Scissors":
                print("Its a tie !!")
            else:
                print(" You won !! ")
    again = ["y","yes","yup","yeah"]
    play=input(" Can you play again ?? {yes or no } >> ").lower()
    if play not in again:
        break