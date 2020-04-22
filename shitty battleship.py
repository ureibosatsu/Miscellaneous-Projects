from random import randint

board = []

for i in range(0,5):
    board.append(["O"]*5)

def print_board(board):
    for i in board:
        print(" ".join(i))
print_board(board)

def random_row(board):
    return randint(0,len(board)-1)
def random_column(board):
    return randint(0,len(board)-1)

ship_row=random_row(board)
ship_column=random_column(board)

for turn in range(4):
    print("Turn ",turn+1)

    guess_row=int(input("Guess row: "))-1
    guess_column=int(input("Guess column: "))-1

    if guess_row == ship_row and guess_column == ship_column:
        print("You sunk my schooner!")
        break
    else:
        if guess_row > 5 or guess_column > 5:
            print("That's not even in the ocean, habibi.")
        elif(board[guess_row][guess_column]=="X"):
            print("You already guessed that!")
        else:
            print("You missed!")
        board[guess_row][guess_column]="X"
        if turn==3:
            print("Game over.")
        else:
            print_board(board)
