#!/usr/bin/python3
import sys


def print_usage_and_exit(message, status_code):
    print(message)
    sys.exit(status_code)

# Function to check if placing a queen at board[row][col] is valid


def is_safe(board, row, col, N):
    # Check for queen in the same column
    for i in range(row):
        if board[i] == col:
            return False
        # Check diagonals
        if abs(board[i] - col) == abs(i - row):
            return False
    return True

# Backtracking function to solve the N Queens problem


def solve_nqueens(N, row, board, solutions):
    if row == N:
        # Once a solution is found, add it to the solutions list
        solutions.append([[i, board[i]] for i in range(N)])
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row] = col
            solve_nqueens(N, row + 1, board, solutions)

# Main function to handle input and solve the problem


def nqueens(N):
    board = [-1] * N  # Array to hold the position of queens
    solutions = []
    solve_nqueens(N, 0, board, solutions)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print_usage_and_exit("Usage: nqueens N", 1)

    # Check if N is a valid integer
    try:
        N = int(sys.argv[1])
    except ValueError:
        print_usage_and_exit("N must be a number", 1)

    # Check if N is greater than or equal to 4
    if N < 4:
        print_usage_and_exit("N must be at least 4", 1)

    # Solve the N-Queens problem
    nqueens(N)
