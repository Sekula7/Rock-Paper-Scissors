from random import choice
from time import sleep
from colorama import Fore, Back, Style, init


choice_list = ['Rock', 'Paper', 'Scissors']
player_score = 0
computer_score = 0

def main(welcome = True):
    global player_score, computer_score # Global variable cuz python cant use player_score or computer_score since its outside of the main function
    init (autoreset = True)
    
    def get_results(player_move, computer_move):
        if player_move == computer_move:
            return "tie"
        elif (player_move == "Rock" and computer_move == "Scissors") or \
             (player_move == "Paper" and computer_move == "Rock") or \
             (player_move == "Scissors" and computer_move == "Paper"):
            return "player_win"
        else:
            return "computer_win"


    #Choices 
    if welcome: # Welcome is used to this message doesnt display every time you ask to play again
        print("Hello player, this is a rock, paper scissors game! Please choose your move: ")

    while True:
        player_move = input("Choose your move Rock, Paper or Scissors: ").strip().capitalize() # Capitalizing moves for better readability
        if player_move in ['Rock', 'Paper', 'Scissors']:
            print(f"You have chosen {player_move}, now the computer will chose its move. ")
            sleep(1)
            computer_move = choice(choice_list)
            print(computer_move)
            break 
        elif player_move == "Lizard":
            print("🦎 You found the secret Lizard! Too bad it's not supported 😄")
        else:
            print("The move is invalid, please reenter one of the choices")

    #Game Logic + Score Tracker
    result = get_results(player_move, computer_move) # Calling the get_results function to see who won
    if result == "player_win":
        player_score += 1
        print(Back.GREEN + Fore.WHITE + f"You win! {player_move} beats {computer_move}.")
    elif result == "computer_win":
        computer_score += 1
        print(Back.RED + Fore.WHITE + f"Computer wins! {computer_move} beats {player_move}.")
    else:  # This case is a tie
        print(Back.YELLOW + Fore.WHITE + f"It's a tie! Both chose {player_move}.")
    
    print(f"Score -> Player {player_score} : Computer {computer_score}")
                
#Ask to play again 
    while True:
        play_again = input("Would you like to play again? Y/N: ")
        if play_again.strip().lower() == 'y':
            print("Awesome! Lets play again.")
            main(welcome=False) # Welcome is now false so the welcome message doesnt display
            return
        elif play_again.strip().lower() == 'n':
            print("Thanks for playing Rock, Paper, Scissors with me. Goodbye!")
            sleep(5) # Sleep 5 is so you can read the message above before the program closes
            return
        else:
            print("Your answer wasnt found in the list of answers. Please insert Y(Yes) or N(No)")           

main()

