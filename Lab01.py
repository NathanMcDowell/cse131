# 1. Name:
#      Nathan McDowell
# 2. Assignment Name:
#      Lab 01: Tic-Tac-Toe
# 3. Assignment Description:
#      Play the game of Tic-Tac-Toe
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part of this assignment was adding checks for improper input. It took me a bit to figure
#       out how to do it, and there were several errors along the way that I had to resolve.
# 5. How long did it take for you to complete the assignment?
#      This took about three and a half hours

import json

# The characters used in the Tic-Tac-Too board.
# These are constants and therefore should never have to change.
X = 'X'
O = 'O'
BLANK = ' '

# A blank Tic-Tac-Toe board. We should not need to change this board;
# it is only used to reset the board to blank. This should be the format
# of the code in the JSON file.
blank_board = [
                BLANK, BLANK, BLANK,
                BLANK, BLANK, BLANK,
                BLANK, BLANK, BLANK ]

test_board = [
                X, O, O,
                X, BLANK, X,
                O, X, BLANK ]
        
def read_board(filename):
    '''Read the previously existing board from the file if it exists.'''
    # Put file reading code here.
    with open(filename, 'r') as filehandle:
        file = json.load(filehandle)
        data = file["board"]
        for i in data:
            if i == " ":
                i = BLANK
        return data
   

def save_board(filename, board):
    '''Save the current game to a file.'''
    board_dict = {"board": board}
    with open(filename, "w") as f:
        json.dump(board_dict, f)

def display_board(board):
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print(f"---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print(f"---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")

def is_x_turn(board):
    '''Determine whose turn it is.'''
    x_count = 0
    o_count = 0
    for i in board:
        if i == "X":
            x_count += 1
        if i == "O":
            o_count += 1
    if x_count <= o_count:
        return True
    else:
        return False

def play_game(board):
    '''Play the game of Tic-Tac-Toe.'''
    print("Enter 'q' to suspend your game. Otherwise, enter a number from 1 to 9")
    print("where the following numbers correspond to the locations on the grid:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 \n")
    print("The current board is:")
    game_input = ""
    while game_done(board, True) == False and game_input != "q":
        if is_x_turn(board):
            turn = X
        else:
            turn = O
        display_board(board)
        game_input = input(f"{turn}> ")
        while game_input != "q" and game_input.isdigit() == False:
            display_board(board)
            print("Please give a proper input.")
            game_input = input(f"{turn}> ")
        if game_input == "q":
            return board
        if 1 <= int(game_input) <= 9 and board[int(game_input) - 1] == " ":
            board[int(game_input) - 1] = turn
        else:
            print("Please give a proper input.")
    return board
        

def game_done(board, message=False):
    '''Determine if the game is finished.
       Note that this function is provided as-is.
       You do not need to edit it in any way.
       If message == True, then we display a message to the user.
       Otherwise, no message is displayed. '''

    # Game is finished if someone has completed a row.
    for row in range(3):
        if board[row * 3] != BLANK and board[row * 3] == board[row * 3 + 1] == board[row * 3 + 2]:
            if message:
                print("The game was won by", board[row * 3])
            return True

    # Game is finished if someone has completed a column.
    for col in range(3):
        if board[col] != BLANK and board[col] == board[3 + col] == board[6 + col]:
            if message:
                print("The game was won by", board[col])
            return True

    # Game is finished if someone has a diagonal.
    if board[4] != BLANK and (board[0] == board[4] == board[8] or
                              board[2] == board[4] == board[6]):
        if message:
            print("The game was won by", board[4])
        return True

    # Game is finished if all the squares are filled.
    tie = True
    for square in board:
        if square == BLANK:
            tie = False
    if tie:
        if message:
            print("The game is a tie!")
        return True


    return False


def display_menu():
    print("Select what you would like to do:")
    print("1. Start a new game")
    print("2. Resume game")
    print("2. Load a saved game")
    print("3. Save current game")
    print("4. Quit")

def main():
    done = False
    board = []
    while done == False:
        display_menu()
        menu_input = input("> ")
        match menu_input:
            case "1":
                print("Starting new game")
                board = play_game(blank_board.copy())
                print(board)
            case "2":
                print("Resuming game")
                if board == []:
                    print("Blank resume")
                    board = play_game(blank_board.copy())
                else:
                    print("play resume")
                    board = play_game(board)
            case "3":
                filename = input("Input file name to load from: ")
                board = read_board(filename)
                board = play_game(board)
            case "4":
                filename = input("Input file name to save to: ")
                save_board(filename, board)
            case "5":
                done = True
    print("Thank you for playing!")

main()