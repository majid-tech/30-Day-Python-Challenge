
def play_game():
    trys = 1
    score = 0

    def computer_choice():
        return 8

    def player_choice():
        player_choice = int(input("Enter a number between 1 and 10: "))
        return player_choice


    while trys < 6:
        if computer_choice() == player_choice():
            score += 1
            print(f"You have scored {score}!")
        else:
            print("Oops! Try again")
            print(f"You have {trys} tries remaining.")
        trys += 1

play_game()
print("Thank you!")