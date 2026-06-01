import pytest
from sudoku import validate_input, validate_coordinate, validate_square, \
    validate_row, validate_column, convert_input

board = \
[[ 7, 2, 3, 0, 0, 0, 1, 5, 9 ],
[ 6, 0, 0, 3, 0, 2, 0, 0, 8 ],
[ 8, 0, 0, 0, 1, 0, 0, 0, 2 ],
[ 0, 7, 0, 6, 5, 4, 0, 2, 0 ],
[ 0, 0, 4, 2, 0, 7, 3, 0, 0 ],
[ 0, 5, 0, 9, 3, 1, 0, 4, 0 ],
[ 5, 0, 0, 0, 7, 0, 0, 0, 3 ],
[ 4, 0, 0, 1, 0, 3, 0, 0, 6 ],
[ 9, 3, 2, 0, 0, 0, 7, 1, 4 ]]

def test_validate_input():
    # Requirement
    assert validate_input('5c') == True
    assert validate_input('c5') == True
    # Boundary
    assert validate_input('a1') == True
    assert validate_input('i9') == True
    # Error
    assert validate_input('e') == False
    assert validate_input('2') == False
    assert validate_input('g10') == False
    assert validate_input('j1') == False

def test_validate_coordinate():
    # input (row, col, board)
    # Requirement
    assert validate_coordinate(0, 3, board) == True
    assert validate_coordinate(8, 5, board) == True
    assert validate_coordinate(4, 0, board) == True
    # Error
    assert validate_coordinate(0, 0, board) == False
    assert validate_coordinate(8, 8, board) == False
    assert validate_coordinate(3, 5, board) == False

def test_validate_square():
    # input (row, col, new_value, board)
    # Requirements
    assert validate_square(4, 4, 8, board) == True
    assert validate_square(2, 2, 1, board) == True
    # Error
    assert validate_square(4, 4, 7, board) == False
    assert validate_square(7, 6, 7, board) == False

def test_validate_row():
    # input (row, new_value, board)
    # Requirements
    assert validate_row(0, 1, board) == True
    assert validate_row(0, 3, board) == True
    assert validate_row(1, 6, board) == True
    # Errors
    assert validate_row(1, 2, board) == False
    assert validate_row(5, 1, board) == False
    assert validate_row(6, 7, board) == False

def test_validate_column():
    # input (col, new_value, board)
    # Requirements
    assert validate_column(0, 8, board) == True
    assert validate_column(1, 7, board) == True
    assert validate_column(2, 3, board) == True
    # Errors
    assert validate_column(0, 7, board) == False
    assert validate_column(7, 4, board) == False
    assert validate_column(8, 9, board) == False

def test_convert_input():
    # returns (row, column)
    # Requirements
    assert convert_input('A3') == (2, 0)
    assert convert_input('3A') == (2, 0)
    assert convert_input('a3') == (2, 0)





pytest.main(["-v", "--tb=line", "-rN", __file__])