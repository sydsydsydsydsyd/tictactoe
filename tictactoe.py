"""
Tic Tac Toe Player
"""

import math
import copy
from random import randint

X = "X"
O = "O"
EMPTY = None


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

    num_Xs = 0
    num_Os = 0
    for i in board:
        for j in i:
            if j == X:
                num_Xs += 1
            if j == O:
                num_Os +=1
    if num_Os == num_Xs:
        return X
    if num_Os < num_Xs:
        return O

    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                act_tup = (i, j)
                actions.add(act_tup)
    return actions

    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    board_copy = copy.deepcopy(board)
    board_copy[action[0]][action[1]] = player(board)
    return board_copy

    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # horizontal
    if board[0][0] == board[0][1] and board[0][1] == board[0][2]:
        return board[0][0]
    elif board[1][0] == board[1][1] and board[1][1] == board[1][2]:
        return board[1][0]
    elif board[2][0] == board[2][1] and board[2][1] == board[2][2]:
        return board [2][0]

    # vertical
    elif board[0][0] == board[1][0] and board[1][0] == board[2][0]:
        return board [0][0]
    elif board[0][1] == board[1][1] and board[1][1] == board[2][1]:
        return board[0][1]
    elif board[0][2] == board[1][2] and board[1][2] == board[2][2]:
        return board[0][2]

    # diagonal
    elif board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[0][0]
    elif board[2][0] == board[1][1] and board[1][1] == board[0][2]:
        return board[2][0]

    else:
        return None


    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if len(actions(board)) == 0:
        return True
    elif winner(board):
        return True
    else:
        return False

    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else: return 0

    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    optimal_action = (None, None)
    if terminal(board):
        optimal_action = optimal_action

    if board == initial_state():
        optimal_action = (randint(0, 2), randint(0, 2))

    elif player(board) == X:
        optimal_action = maxValue(board)[0]

    elif player(board) == O:
        optimal_action = minValue(board)[0]

    return optimal_action



def maxValue(board):

    if terminal(board):
        return (None, utility(board))

    max_val = -math.inf
    optimal_action = None
    for action in actions(board):
        v = minValue(result(board, action))[1]
        if v > max_val:
            max_val = v
            optimal_action = action
    return (optimal_action, max_val)

def minValue(board):
    if terminal(board):
        return (None, utility(board))
    min_val = math.inf
    optimal_action = None
    for action in actions(board):
        v = maxValue(result(board, action))[1]
        if v < min_val:
            min_val = v
            optimal_action = action
    return (optimal_action, min_val)

    raise NotImplementedError
