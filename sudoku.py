# 1. Name:
#      Nathan McDowell
# 2. Assignment Name:
#      Lab 06 : Sudoku Program
# 3. Assignment Description:
#      This program lets the user play Sudoku using boards extracted from json files.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part was getting the test cases working. Here is the issue. The 
# game has you input coordinates like "A1" for ease of use. The program converts this
# into number coordinates, and those are used for all the validation. That means that
# all of the validation function tests intake index numbers, which is ahrd to read.
# I fixed this by making a "testing_display_board" function that displays index numbers
# for ease of use while making tests.
# 5. How long did it take for you to complete the assignment?
#      About 3.5 hours

import json

LETTERS = ['a','b','c','d','e','f','g','h','i']

def get_file_name():
    filename = input("Input filename: ")
    return filename

def read_board(filename):
    with open(filename, "r") as f:
        data = json.load(f)
    return data

def save_board(data, filename):
    with open(filename, "w") as f:
        json.dump(data, f)

def display_board(board):
    '''Displays a list of lists as a Sudoku grid with coordinates.'''
    print('   A B C D E F G H I')
    separator = '  |  |   '
    for row in range(9):
        if row == 3 or row == 6:
            print('   -----+-----+-----')
        print(row + 1, end='  ')
        for column in range(9):
            if board[column][row] != 0:
                print(f'{board[column][row]}', end='')
            else:
                print(' ', end='')
            print(separator[column],end='')
        print()
    print()

def testing_display_board(board):
    '''Displays the board with index numbers instead of grid coordinates.'''
    print('   0 1 2 3 4 5 6 7 8')
    separator = '  |  |   '
    for row in range(9):
        if row == 3 or row == 6:
            print('   -----+-----+-----')
        print(row, end='  ')
        for column in range(9):
            if board[column][row] != 0:
                print(f'{board[column][row]}', end='')
            else:
                print(' ', end='')
            print(separator[column],end='')
        print()
    print()

def validate_input(coordinate):
    '''Returns if the coordinate string is two characters long, contains a digit, 
    and contains a letter from the coordinate options.'''
    return (
        len(coordinate) == 2 and
        any(c.isdigit() for c in coordinate) and
        any((c in LETTERS) for c in coordinate)
    )

def validate_value(value):
    '''Returns whether a value is a viable integer to put in a sudoku board.'''
    if value.isdigit():
        return 1 <= int(value) <= 9
    return False

def validate_coordinate(row, col, board):
    '''Returns whether a coordinate is empty or not.'''
    return board[col][row] == 0

def validate_square(row, col, new_value, board):
    '''Returns whether a value isn't used in the coordinate's square or not.'''
    square_row = (row // 3) * 3
    square_column = (col // 3) * 3
    for r in range(square_row, square_row+3):
        for c in range(square_column, square_column+3):
            if board[c][r] == new_value:
                return False
    return True

def validate_row(row, new_value, board):
    '''Returns whether a value isn't used in the coordinate's row or not.'''
    for col in board:
        if col[row] == new_value:
            return False
    return True

def validate_column(col, new_value, board):
    '''Returns whether a value isn't used in the coordinate's column or not.'''
    for i in board[col]:
        if i == new_value:
            return False
    return True

def convert_input(raw_input):
    '''Returns a tuple of integers (row, column) converted from 
    a two character coordinate string ("A3"))'''
    raw_list = [raw_input[0], raw_input[1]]
    column = 0
    column_letter = 'A'
    if raw_list[0].isdigit():
        column_letter = raw_list[1]
        row = int(raw_list[0]) - 1
    elif raw_list[1].isdigit():
        column_letter = raw_list[0]
        row = int(raw_list[1]) - 1
    for l in LETTERS:
        if column_letter.lower() == l:
            column = LETTERS.index(l)
    return row, column

def update_square(row, col, board, new_square_value):
    '''Updates a value on the board.'''
    board[col][row] = new_square_value

def play_the_game(board):
    '''Main game loop. Returns the board when the user quits.'''
    while True:
        display_board(board)
        print('Specify a coordinate to edit or "q" to save and quit')
        user_input = input('> ').lower()
        if user_input == 'q':
            return board
        if validate_input(user_input):
            row, col = convert_input(user_input)
            if validate_coordinate(row, col, board):
                new_value = input(f'What number goes in {user_input}? ')
                if validate_value(new_value):
                    new_value = int(new_value)
                    if validate_column(col, new_value, board) and validate_row(row, new_value, board) and validate_square(row, col, new_value, board):
                        update_square(row, col, board, new_value)
                    else:
                        print("Value already used.")
                else:
                    print("Input a number between 1 and 9")
            else:
                print("Square already filled.")
        else:
            print("Invalid Input.")

def main():

    data = read_board(get_file_name())
    board = play_the_game(data['board'])
    filename = input('Input the filename to save to: ')
    data = {'board': board}
    save_board(data, filename)
    
if __name__ == "__main__":
    main()
