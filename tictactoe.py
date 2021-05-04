"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

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
    x = y = 0
    for i in board:
        for j in i:
            if j == X:
                x += 1
            elif j == O:
                y += 1
    return O if x > y else X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    result = set()
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == EMPTY:
                # print(i, j)
                result.add((i, j))
    return result


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = deepcopy(board)
    i, j = action
    if new_board[i][j] != EMPTY:
        raise Exception("incorrect action!")
    new_board[i][j] = player(new_board)
    return new_board


def checkwin(board, player):
    count = 0

    # Check rows
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == player: count += 1
            else: break
        if count == 3: return True
        count = 0
    
    # Check Columns
    for i in range(len(board)):
        for j in range(len(board)):
            if board[j][i] == player: count += 1
            else: break
        if count == 3: return True
        count = 0

    # check diagonal right
    j = 0
    for i in range(len(board)):
        if board[i][j] == player: count += 1
        else: break
        j += 1
    if count == 3: return True
    count = 0

    # check diagonal left
    j = 2
    for i in range(len(board)):
        if board[i][j] == player: count += 1
        else: break
        j -= 1
    if count == 3: return True
    return False


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if checkwin(board, X) == True:
        return X
    elif checkwin(board, O) == True:
        return O
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    if (not any(EMPTY in sublist for sublist in board) and winner(board) is None):
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def max_value(board):
    v = -math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v


def min_value(board):
    v = math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    turn = player(board)
    if turn == X:
        options = []
        for action in actions(board):
            v = min_value(result(board, action))
            # print(action, v)
            if v == 1:
                # print("yaha se")
                return action
            options.append([v, action])
        for option in options:
            if option[0] == 0:
                return option[1]
        return options[0][1]
    elif turn == O:
        options = []
        for action in actions(board):
            v = max_value(result(board, action))
            if v == -1:
                return action
            options.append([v, action])
        for option in options:
            if option[0] == 0:
                return option[1]
        return options[0][1]
