from game import RockPaperScissors

def main():
    game = RockPaperScissors()
    print("*** ROCK PAPER SCISSORS GAME ***")
    while True:
        print("\nChoose:")
        print("Rock")
        print("Paper")
        print("Scissors")
        user_choice = input("Enter your choice: ").lower()
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice! Please try again.")
            continue
        computer_choice = game.get_computer_choice()
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        result = game.determine_winner(user_choice, computer_choice)
        if result == "tie":
            print("It's a Tie!")
        elif result == "user":
            print("You Win!")
        else:
            print("Computer Wins!")
        print("\n===== SCORE =====")
        print(f"User Score     : {game.user_score}")
        print(f"Computer Score : {game.computer_score}")
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("\nThanks for playing!")
            break
if __name__ == "__main__":
    main()