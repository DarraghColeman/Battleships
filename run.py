#Legend
#X for placing ship and hit battleship
#' ' for available space
#'-' for missed shot

from random import randint

hidden_board = [[' '] * 5 for x in range(5)]
guess_board = [[' '] * 5 for x in range(5)]

letters_to_numbers = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, }


def print_board(board):
    """
    Game board layout
    """
    print('  A B C D E')
    print(' ----------')
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1


def create_ships(board):
    """
    Adds computer's random ship locations.
    """
    for ship in range(5):
        ship_row, ship_column = randint(0,4), randint(0,4)
        while board[ship_row][ship_column] == 'X':
            ship_row, ship_column = randint(0,4), randint(0,4)
        board[ship_row][ship_column] = 'X'


def get_ship_location():
    """
    Adds user input and error messages when user inputs incorrect data.
    """
    row = input('Please enter a ship row 1-5: ')
    while row not in '12345':
        print('Please enter a valid row')
        row = input('Please enter a ship row 1-5: ')
    column = input('Please enter a ship column A-E: ').upper()
    while column not in 'ABCDE':
        print('Please enter a valid column')
        column = input('Please enter a ship column A-E: ').upper()
    return int(row) - 1, letters_to_numbers[column]


def count_hit_ships(board):
    """
    Counts successful hits and adds an extra turn
    """
    count = 0
    for row in board:
        for column in row:
            if column == 'X':
                count += 1
    return count


create_ships(hidden_board)
turns = 10
while turns > 0:
    print('Welcome to Battleships')
    print_board(guess_board)
    row, column = get_ship_location()
    if guess_board[row][column] == '-':
        print('You already guessed that')
    elif hidden_board[row][column] == 'X':
        print('Congratulations, you have hit the battleship!')
        guess_board[row][column] = 'X'
        turns -= 1
    else:
        print('Sorry, you missed')
        guess_board[row][column] = '-'
        turns -= 1
    if count_hit_ships(guess_board) == 5:
        print('Congratulations, you have sunk all the battleships!')
        break
    print('You have ' + str(turns) + ' turns remaining')
    if turns == 0:
        print('Sorry, you ran out of turns, game over!')
        break

#while turns > 0:
