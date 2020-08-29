"""
Tic Tac Toe Player
"""

import math

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
                num_Ys +=1
    if num_Ys == num_Xs:
        return X
    if num_Ys < num_Xs:
        return Y

    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    actions = set()
    for i in board:
        for j in i:
            if j == EMPTY:
                actions += (i, j)
    return actions

    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    board_copy = copy.deepcopy(board)
    board_copy[i][j] = action
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
        return board[0][0]
    elif board[2][0] == board[2][1] and board[2][1] == board[2][2]:
        return board [0[0]]

    # vertical
    elif board[0][0] == board[1][0] and board[1][0] == board[2][0]:
        return board [0[0]]
    elif board[0][1] == board[1][1] and board[1][1] == board[2][1]:
        return board[0][0]
    elif board[0][2] == board[1][2] and board[1][2] == board[2][2]:
        return board[0][0]

    # diagonal
    elif board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[0][0]
    elif board[2][0] == board[1][1] and board[1][1] == board[0][2]:
        return board[0][0]

    else:
        return None


    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) or len(actions(board)) == 0:
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
    elif winner(board) == Y:
        return -1
    else: return 0

    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    score_list = []
    # turn = player(board)
    actions = actions(board)
    for action in actions:
        score = 0
        result_board = result(board, action)
        if terminal(result_board):
            score += utility(result_board)
        else: minimax(result_score)
        score_list.append(score)
    min_score = 0
    for score in score_list:
        if score < min_score:
            min_score = score
    actions[score_list.index(min_score)] = optimal_action
    return optimal_action




    raise NotImplementedError
