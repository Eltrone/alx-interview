#!/usr/bin/python3
"""
This module solves the N Queens problem using backtracking.
"""

import sys

def print_board(board):
    """Prints the current board configuration."""
    print([list(b) for b in board])

def is_safe(board, row, col):
    """Checks if it's safe to place a queen at board[row][col]."""
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve_nqueens(board, col):
    """Uses backtracking to find all solutions."""
    if col >= len(board):
        print_board([(i, board[i].index(1)) for i in range(len(board))])
        return
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            solve_nqueens(board, col + 1)
            board[i][col] = 0

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize the board
    board = [[0]*n for _ in range(n)]
    solve_nqueens(board, 0)

if __name__ == "__main__":
    main()
