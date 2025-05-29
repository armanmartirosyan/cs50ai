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
    x_count: int = 0
    o_count: int = 0
    for row in board:
        for col in row:
            if col == X:
                x_count += 1
            elif col == O:
                o_count += 1

    return X if x_count == o_count else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    res: set[tuple] = set()
    for row_indx, row in enumerate(board):
        for col_indx, col in enumerate(row):
            if col == EMPTY:
               res.add((row_indx, col_indx))
    return res


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    copy_board: list[list[str]] = [row.copy() for row in board]
    turn: str = player(board)
    if (action[0] < 0 or action[0] > 2 or action[1] < 0 or action[1] > 2):
        raise Exception(f"Cell ({action[0]}, {action[1]}) is already occupied.")
    if (copy_board[action[0]][action[1]] == EMPTY):
        copy_board[action[0]][action[1]] = turn
    else:
        raise Exception(f"Cell ({action[0]}, {action[1]}) is already occupied.")

    return copy_board



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    winning_line = [
        #Rows
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],

        #Cols
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
    
        #Diagonal
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)],
    ]

    for line in winning_line:
        [a, b, c] = line
        first = board[a[0]][a[1]]
        if (first and first == board[b[0]][b[1]] and first == board[c[0]][c[1]]):
            return first
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if (winner(board=board)):
        return True

    for row in board:
        for col in row:
            if (col == EMPTY):
                return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    the_winner = winner(board=board)
    if (the_winner == X):
        return 1
    elif (the_winner == O):
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board=board):
        return None
    if player(board) == X:
        value, move = max_value(board)
        return move
    else:
        value, move = min_value(board)
        return move


def max_value(board):
    if terminal(board):
        return utility(board), None
    v = -math.inf
    best_action = None
    for action in actions(board):
        min_v, _ = min_value(result(board, action))
        if min_v > v:
            v = min_v
            best_action = action
            if v == 1:
                break
    return v, best_action


def min_value(board):
    if terminal(board):
        return utility(board), None
    v = math.inf
    best_action = None
    for action in actions(board):
        max_v, _ = max_value(result(board, action))
        if max_v < v:
            v = max_v
            best_action = action
            if v == -1:
                break
    return v, best_action


# board = initial_state()
# board[0][0] = X
# board[0][1] = O
# board[1][1] = X
# board[2][0] = O
# # board[2][2] = X


# for row in board:
#     print (row)

# print ("Turn to move: ", player(board=board))
# print("All available actions: ", actions(board=board))
# print ("Result after move: ", result(board=board, action=(0,2)))
# print ("Winner is: ", winner(board=board))
# print ("Is the game over: ", terminal(board=board))
# print ("The utility: ", utility(board=board))