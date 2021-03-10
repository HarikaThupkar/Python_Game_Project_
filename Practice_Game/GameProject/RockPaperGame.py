#Rock, Paper, Scissors Game

# importing required random module

from random import randint

moves = ['Rock', 'Paper', 'Scissors']


def ask_move(player=False):
    if player:
        return moves.index(moves[int(input("Pick a move, 1: %s, 2: %s, 3: %s"
                                           % (moves[0], moves[1], moves[2]))) - 1]) + 1
    else:
        return randint(1, 3)


def calculate_score(p1, p2):
    movescore = p1 -p2
    if movescore == 0:
        print("Tie!")
    elif movescore in (1, -2):
        print("Win!")
    else:
        print("You lose!")

if __name__ == "__main__":
    print("Welcome to the Rock, Paper, Scissors game!")
    while True:
        print("Player 1:\n")
        one = ask_move(True)
        two = ask_move()
        calculate_score(one, two)
        try:
            break_ = input("Would you like to play again?\nEnter [1] if you would like to, else press enter.")
            if 1 == int(break_):
                print("Thank you for playing!")
            break
        except ValueError:
            print("Ok, here we go again\n")