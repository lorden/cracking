# Assuming a 3x3 Tic-Tac-Toe board


def is_winner(board):
    # Check rows
    for i in xrange(0, 3):
        if board[i][0] is not None and\
                (board[i][0] == board[i][1] == board[i][2]):
            return True

    # Check cols
    for i in xrange(0, 3):
        if board[0][i] is not None and\
                (board[0][i] == board[1][i] == board[2][i]):
            return True

    # Check diagonals
    if (board[0][0] is not None and
            (board[0][0] == board[1][1] == board[2][2])) or\
            (board[0][2] is not None and
            (board[0][2] == board[1][1] == board[2][0])):
        return True

    return False

boards = [
    [[0, 1, 0], [1, 1, 0], [1, 0, 1]],
    [[1, 0, 1], [None, 0, None], [1, 0, None]],
    [[None, None, None], [1, 1, 0], [1, 0, 1]]
]

for board in boards:
    if is_winner(board):
        print "Winner!"
    else:
        print "No winner :("
