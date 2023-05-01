"""Game of TicTacToe."""

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def print_board(board):
    """Board Design."""
    print(board['top-L'] + ' |' + board['top-M'] + ' |' + board['top-R'])
    print('--+--+--')
    print(board['mid-L'] + ' |' + board['mid-M'] + ' |' + board['mid-R'])
    print('--+--+--')
    print(board['low-L'] + ' |' + board['low-M'] + ' |' + board['low-R'])

def game_logic():
    """Game Logic."""
    turn = "X"
    for i in range(9):
        print_board(theBoard)
        move = input('Turn for ' + turn + ' on which space?: ')
        theBoard[move] = turn
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
    print_board(theBoard)

game_logic()
