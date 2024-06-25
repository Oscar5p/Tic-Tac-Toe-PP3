from helpers import draw_board, check_turn, check_for_win
import os

spots = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5",
         6: "6", 7: "7", 8: "8", 9: "9"}

playing = True
complete = False
turn = 0
prev_turn = -1

# Color of green text when there is a winner
GREEN = '\033[92m'
RESET = '\033[0m'

# Smiling emoji
SMILING_EMOJI = '😊'

# Intro message
print("Hi and welcome to my Tic-Tac-Toe game!")
print("The rules are simple: get 3 in a row either horizontally,vertically, or diagonally.")
print("Best of luck!")
input("Press Enter to start the game...")


while playing:
    # Reset the screen
    os.system('cls' if os.name == 'nt' else 'clear')
    draw_board(spots)
    # If an invalid turn occurred, let the player know
    if prev_turn == turn:
        print("Invalid spot selected, please pick another.")
    prev_turn = turn
    print("Player" + str((turn % 2) + 1) +
          "'s turn: Pick your spot or press q to quit")
    # Get Input from the player
    choice = input()
    if choice == 'q':
        playing = False
        # Check if the player gave a number from 1-9
    elif str.isdigit(choice) and int(choice) in spots:
        # Check if the spot has already been taken
        if not spots[int(choice)] in {"X", "0"}:
            # Valid input, update the board
            turn += 1
            spots[int(choice)] = check_turn(turn)

if check_for_win(spots):
    playing, complete = False, True
if turn > 8:
    playing = False

# Out of the loop, print the results
# Draw the board one last time.
os.system('cls' if os.name == 'nt' else 'clear')
draw_board(spots)
# If there was a winner, say who won
if complete:
    if check_turn(turn) == 'X':
        print(GREEN + "Player 1 Wins!" + SMILING_EMOJI + RESET)
    else:
        print(GREEN + "Player 2 Wins!" + SMILING_EMOJI + RESET)
else:
    # Tie Game
    print("No Winner")

    print("Thanks for playing!")

    # The user can rate my game afterwards
    rating = input(
        "You can rate my game from 1 to 5 (1 being worst and 5 being best, Thank you for playing!): ")
    if rating.isdigit() and 1 <= int(rating) <= 5:
        print(f"Thank you for giving med feedback and rating! {rating}/5!")
    else:
        print("Invalid rating. Thanks again for playing!")


# https://www.youtube.com/watch?v=Q6CCdCBVypg&ab_channel=CDcodes
# This is the walkthrough for the tic tac toe game

# My own code is the color when you win, the emoji and the intro message when you start the game
