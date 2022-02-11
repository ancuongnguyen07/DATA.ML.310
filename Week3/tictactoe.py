"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None
LENGTH = 3

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    xCount = oCount = 0
    for row in range(LENGTH):
        for col in range(LENGTH):
            if board[row][col] == X:
                xCount += 1
            elif board[row][col] == O:
                oCount += 1
    
    if xCount > oCount:
        return O
    return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    result = set()
    for row in range(LENGTH):
        for col in range(LENGTH):
            if board[row][col] == EMPTY:
                coordinates = (row, col)
                result.add(coordinates)
        
    return result




def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    row, col = action

    if board[row][col] != EMPTY:
        raise ValueError
    
    p = player(board)
    newBoard = deepcopy(board)
    if p == X:
        newBoard[row][col] = X
    else:
        newBoard[row][col] = O
    return newBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check horizontally
    for row in range(LENGTH):
        winnerExist = True
        for col in range(LENGTH - 1):
            if board[row][col] != board[row][col + 1]:
                winnerExist = False
                break

        if winnerExist:
            return board[row][0]

    # Check vertically
    for col in range(LENGTH):
        winnerExist = True
        for row in range(LENGTH - 1):
            if board[row][col] != board[row + 1][col]:
                winnerExist = False
                break

        if winnerExist:
            return board[0][col]

    # Check left diagonally
    row = col = 0
    winnerExist = True
    while row < LENGTH - 1 and col < LENGTH - 1:
        if board[row][col] != board[row + 1][col + 1]:
            winnerExist = False
            break
        row += 1
        col += 1

    if winnerExist:
        return board[row][col]

    # Check right diagonally
    row = 0
    col = 2
    winnerExist = True
    while row < LENGTH - 1 and col > 0:
        if board[row][col] != board[row + 1][col - 1]:
            winnerExist = False
            break
        row += 1
        col -= 1

    if winnerExist:
        return board[row][col]

    # There is no winner, the game needed to be continued
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        # If someone has won
        return True
    
    for row in range(LENGTH):
        for col in range(LENGTH):
            if board[row][col] == EMPTY:
                return False
    # There is no more empty cells to be filled
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    champion = winner(board)
    if champion == X:
        return 1
    elif champion == O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    p = player(board)
    final_act = ()
    if p == X:
        # max player
        comp = -2
    else:
        # min player
        comp = 2

    if p == X:
        point, act = max_value(board)
        if point == 1:
            return act
        if point > comp:
            comp = point
            final_act = act
    else:
        point, act = min_value(board)
        if point == -1:
            return act
        if point < comp:
            comp = point
            final_act = act
    return final_act

def min_value(board):
    if terminal(board):
        return [utility(board), None]

    min_point = 2
    final_act = ()
    for act in actions(board):
        point, _ = max_value(result(board, act))
        if point <= min_point:
            min_point = point
            final_act = act
        if min_point == -1:
            break
    return [min_point, final_act]

def max_value(board):
    if terminal(board):
        return [utility(board), None]

    max_point = -2
    final_act = ()
    for act in actions(board):
        point, _ = min_value(result(board, act))
        if point >= max_point:
            max_point = point
            final_act = act
        if max_point == 1:
            break
    return [max_point, final_act]
