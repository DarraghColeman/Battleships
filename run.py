#Legend
#X for placing ship and hit battleship
#' ' for available space
#'-' for missed shot

from random import randint

hidden_board = [[' '] * 8 for x in range(8)]
guess_board = [[' '] * 8 for x in range(8)]

letters_to_numbers = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, }


def print_board(board):
    print('   A B C D E F G H')
    print('   ---------------')
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1


def create_ships(board):
    for ship in range(5):
        ship_row, ship_column = randint(0,7), randint(0,7)
        while board[ship_row][ship_column] == 'X':
            ship_row, ship_column = randint(0,7), randint(0,7)
        board[ship_row][ship_column] = 'X'


def get_ship_location():
    row = input('Please enter a ship row 1-8: ')
    while row not in '12345678':
        print('Please enter a valid row')
        row = input('Please enter a ship row 1-8: ')
    column = input('Please enter a ship column A-H: ').upper()
    while column not in 'ABCDEFGH':
        print('Please enter a valid column')
        column = input('Please enter a ship column A-H: ').upper()
    return int(row) - 1, letters_to_numbers[column]


def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == 'X':
                count += 1
    return count


create_ships(hidden_board)
print_board(hidden_board)
turns = 10
while turns > 0:
    print('Welcome to Battleships')
    print(guess_board)
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
