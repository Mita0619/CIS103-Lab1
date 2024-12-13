# Romain Tranchant - Elysee Fleurant - Ashley Nunez - Edward McBride
# Instructor: MD Ali
# CIS 103: Fundamentals of Programming
# Lab 4: Python Practice – Group Assignment
# Due Date: 10/05/2024 @ 11:59pm
# Presentation Date: 09/28/2024 @ 10:00am


# Rock, Paper, Scissors Game
# • Build a two-player or player-vs-computer Rock, Paper, Scissors game. The game should allow for
# multiple rounds and declare a winner at the end.
# • Bonus: Keep track of player scores and display a final scoreboard.
# • Focus Areas: Functions, loops, conditional statements, and randomness (random module).


###############################################################################################


# Import the random module for the computer choices
import random
# Define the function to choose the game mode
def choose_game():
# Start a while loop that allows the user to choose a game mode, come out of this game mode and
# choose another game mode
    while True:
# Print a greeting message and the game modes
        print("Welcome to Rock, Paper, Scissors!")
        print("What game do you want to play?")
        print("1. Player vs Player")
        print("2. Player vs Computer")
        print("3. Computer vs Computer")
        print("4. Exit the game")
# Use the try block to handle any errors in the inputs
        try:
# Take the user input and return a game as a result
            game_choice = int(input("Select your game by pressing 1, 2, 3 or 4 to exit :"))
            if game_choice == 1:
# Call the player_vs_player function if the user input is 1, when the user exits the player_vs_player
# function, the continue statement will skip the rest of the program and go back to the menu to choose a game
                player_vs_player()
                continue
# Call the user_vs_computer function if the user's choice is 2
            if game_choice == 2:
                user_vs_computer()
                continue
# Call the computer_vs_computer function if the user's choice is 3
            if game_choice == 3:
                computer_vs_computer()
                continue
# If te user's choice is 4, print a farewell message and exit the loop through the break statement
            if game_choice == 4:
                print("Thank you for playing")
                break
# if the user's choice is not between 1 and 4, print an "Invalid game choice" message and ask the user
# to try again
            if game_choice != [1, 2, 3, 4]:
                print("Invalid game choice")
                print("Try again")
                continue
# If any errors happened during the user input, the except block would catch it
# and return an invalid choice message and ask the user to try again
        except ValueError:
            print("Invalid game choice")
            print("Try again")
            continue


# Start a game function
def player_vs_player():
# Show a greeting message and explain the rules of the game
    print("Welcome to Rock, Paper, Scissors, Player vs Player!")
    print("First player to win 3 rounds wins the game")
    print("Select your weapon by pressing 1, 2, or 3")
    print("Press 4 to exit the game")
# These variables are created to keep the players' scores before the while loop in order for the
# scores to be updated, instead of being set with the same value if they were within the while loop
    score_player1 = 0
    score_player2 = 0
# Start a while loop, allowing the players to play multiple rounds until the score of 3 is met, or if
# a player decides to exit the game
    while True:
# Print the players options
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Exit")
# Use the try block to handle any errors in the player's input
        try:
# Take the player 1 input as an integers, the use of the integers, 1, 2, 3 and 4, instead of
# Rock, Paper or scissors reduce the errors that may happen during the players input
            player1_choice = int(input("Player 1, select a weapon! Press 4 to exit :"))
# If player 1 chooses to exit the game, the score of player 1 and player 2 will be displayed,
# and a winner will be chosen depending on which player has a greater score, and print a message to
# thank the players for participating
            if player1_choice == 4:
                print(f"Score: Player 1: {score_player1}  Player 2: {score_player2}")
                if score_player1 > score_player2:
                    print("Player 1 is the winner!")
                    print("Thank you for playing Rock, Paper, Scissors")
# If the scores are tied, no winners are announced and print a "It's a draw!" message
                elif score_player1 == score_player2:
                    print("It's a draw!")
                    print("Thank you for playing Rock, Paper, Scissors")
                elif score_player2 > score_player1:
                    print("Player 2 is the winner!")
                    print("Thank you for playing Rock, Paper, Scissors")
# After the winner is chosen, if there is one, print a farewell message and the break statement exit
# the loop and ends the game
                print("Goodbye")
                break
# Repeat the same process for the player 2 input if the input is 4
            player2_choice = int(input("Player 2, select a weapon! Press 4 to exit:"))
            if player2_choice == 4:
                print(f"Score: Player 1: {score_player1}  Player 2: {score_player2}")
                if score_player1 > score_player2:
                    print("Player 1 is the winner!")
                elif score_player1 == score_player2:
                    print("It's a draw!")
                elif score_player2 > score_player1:
                    print("Player 2 is the winner!!")
                    print("Thank you for playing Rock, Paper, Scissors")
                print("Goodbye")
                break
# If any errors happened during any players inputs, the except block would catch it
# and return an invalid choice message and skips the rest of the program through the continue statement
        except ValueError:
            print("Invalid choice! Please select between 1 and 4.")
            continue
# If a player's choice is a number but not between 1, 2, or 3, print an invalid choice message
# and skips the rest of the program through the continue statement
        if player1_choice not in [1, 2, 3] or player2_choice not in [1, 2, 3]:
            print("Invalid choice! Please select between 1 and 4.")
            continue
# The next three elif statement are for winning combinations for player 1, taking the input of the
# two players, increasing the variable score_player1 by 1, declaring player 1 as the winner, and
# print the updated scores
        elif player1_choice == 1 and player2_choice == 3:
            score_player1 += 1
            print("Player 1 wins this round!")
            print(f"Score: Player 1: {score_player1}  Player 2: {score_player2}")

        elif player1_choice == 2 and player2_choice == 1:
            score_player1 += 1
            print("Player 1 wins this round!")
            print(f"Score: Player 1: {score_player1}  Player 2: {score_player2}")

        elif player1_choice == 3 and player2_choice == 2:
            score_player1 += 1
            print("Player 1 wins this round!")
            print(f"Score: Player 1: {score_player1}  Player 2: {score_player2}")
# If the players' choices are the same, print a "It's a draw!" message a print the current scores
        elif player1_choice == player2_choice:
            print("It's a draw!")
            print(f"Score: Player 1: {score_player1}  Player 2: {score_player2}")
# If player 1 is not the winner, and the choices are not similar, player 2 is declared winner, the
# score of player 2 is increased by 1 and print the updated scores
        else:
            score_player2 += 1
            print("Player 2 wins this round!")
            print(f"Score: Player 1: {score_player1}  Player 2: {score_player2}")
# When player 1 score or player 2 score reaches 3, this player is declared winner of the game, print
# a message to thank the players for participating and print another farewell message. The break statement
# exit the loop and ends the game
        if score_player1 == 3:
            print("Player 1 is the winner!")
            print("Thank you for playing Rock, Paper, Scissors")
            print("Goodbye")
            break

        if score_player2 == 3:
            print("Player 2 is the winner!")
            print("Thank you for playing Rock, Paper, Scissors")
            print("Goodbye")
            break


# Define the user vs computer function
def user_vs_computer():
    # Show a greeting message and explain the rules of the game
    print("Welcome to Rock, Paper, Scissors, Player vs Computer(Kilroy)!")
    print("First player to win 3 rounds wins the game")
# Assign the boolean value True to the variable playing
    playing = True
# These variables are created to keep the players' scores before the while loop in order for the
# scores to be updated, instead of being set with the same value if they were within the while loop
    user_score = 0
    computer_score = 0
# Start a while loop, allowing the players to play multiple rounds until the score of 3 is met, or if
# a player decides to exit the game
    while playing:
# Use the try block to handle any errors in the player's input
        try:
# Get the user input, choices are rock, paper, scissors, or q to quit the game
            user_action = input("Choose your weapon (rock, paper, scissors)or q to quit:").lower()
# If the user choose to quit, print the score of the game and choose a winner depending on the score
# of the player and the computer and the break statement terminates the game
            if user_action == "q":
                print(f"Score: Player: {user_score} Kilroy: {computer_score}")
                if user_score > computer_score:
                    print("You win")

                if user_score == computer_score:
                    print("It's a draw")

                if user_score < computer_score:
                    print("K.O. You lose the game")
                print("Don't be afraid to come back for more")
                break
# If any errors happened during any players inputs, the except block would catch it
# and return an invalid choice message and skips the rest of the program through the continue statement
        except ValueError:
            print("Invalid choice")
            continue
# The possibles choices for the user are rock, paper, scissors ,and q but the possibles choices for
# the computer are only rock, paper, or scissors, only the user can quit the game
        possible_actions = ["rock", "paper", "scissors", "q"]
        computer_possible_actions = ["rock", "paper", "scissors"]
# If the user input is not in the possible action, print an invalid choice message and the continue
# statement skips the rest of the program to restart the loop
        if user_action not in possible_actions:
                print("Invalid choice")
                continue
# The computer choice is a random choice made from the computer possible actions
        computer_action = random.choice(computer_possible_actions)
# Print the user and the computer choices
        print(f"Your weapon {user_action}")
        print(f"Kilroy's weapon {computer_action}")
# If the user's choice and the computer's choice are the same , print a "it's a draw" message and
# no points are added
        if user_action == computer_action:
            print("it's Draw!")
# These are the three combinations that make the user as a winner, increase the user's scobe by 1 and
# print a "You win" message
        elif user_action == "rock" and computer_action == "scissors":
            print("You Win!")
            user_score += 1
        elif user_action == "paper" and computer_action == "rock":
            print("You Win!")
            user_score += 1
        elif user_action == "scissors" and computer_action == "paper":
            print("You Win!")
            user_score += 1
# If it is not a draw and the user is not the winner, the computer is the winner, print a "K.O you lose"
# message and increase the computer score by 1
        else:
            print("K.O. You Lose")
        computer_score += 1
# Print the updated scores after a winner is chosen
        print(f"Score: User: {user_score}  Computer: {computer_score}")
# When the user score or the computer score reaches 3, this player is declared winner of the game. The playing
# variable turn False and the loop terminates
        if user_score == 3:
            print("You are the winner!")
            playing = False
            print("Don't be afraid to come back for more")
        if computer_score == 3:
            print("Kilroy is the winner!")
            playing = False
            print("Don't be afraid to come back for more")



# Define the computer vs computer function
def computer_vs_computer():
    # Show a greeting message and explain the rules of the game
    print("Welcome to Rock, Paper, Scissors, Computer 1 vs Computer 2!")
    print("First to win 10 rounds wins the game")
# Set the computer1 and computer2 scores
    computer1_score = 0
    computer2_score = 0
# Start a while loop to allow multiple rounds
    while True:
# Set the possible choices
        possible_choices = ["Rock", "Paper", "Scissors"]
# The choices of computer1 and computer2 are made randomly from the list of possibles choices
        computer1_choice = random.choice(possible_choices)
        computer2_choice = random.choice(possible_choices)
# Print the choices made by the computers
        print(f"Computer 1 chose {computer1_choice} and Computer 2 chose {computer2_choice}")
# Winning combinations for computer1, print a "Computer 1 wins" message and increase the computer1' score
# by 1
        if computer1_choice == "Rock" and computer2_choice == "Scissors":
            computer1_score += 1
            print("Computer 1 wins")
        elif computer1_choice == "Paper" and computer2_choice == "Rock":
            computer1_score += 1
            print("Computer 1 wins")
        elif computer1_choice == "Scissors" and computer2_choice == "Paper":
            computer1_score += 1
            print("Computer 1 wins")
# If the computers' choice are the same , print a "it's a draw" message and
# no points are added
        elif computer1_choice == computer2_choice:
            print("It's a draw")
# if computer1 is not the winner and it is not a draw, computer2 is the winner and increase its score by 1
        else:
            computer2_score += 1
            print("computer 2 wins")
# Print the updated scores after a winner is chosen
        print(f"Score: Computer 1: {computer1_score}  Computer 2: {computer2_score}")
# When a computer score reaches 10, this computer is declared winner of the game. The break statement
# terminates the loop
        if computer1_score == 10:
            print("Computer 1 is the winner")
            break
        if computer2_score == 10:
            print("Computer 2 is the winner")
            break

# Call the choose_game function to start the game
choose_game()
