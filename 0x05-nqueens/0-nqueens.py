import sys

def is_safe(board, row, col, n):
    # Check for another queen in the same column
    for i in range(row):
        if board[i] == col:
            return False
    
    # Check for another queen in the upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if i < row and board[i] == j:
            return False

    # Check for another queen in the upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if i < row and board[i] == j:
            return False

    return True

def solve_nqueens(n, row, board, solutions):
    if row == n:
        # Add a solution when all queens are placed
        solutions.append([[i, board[i]] for i in range(n)])
        return
    
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col  # Place a queen
            solve_nqueens(n, row + 1, board, solutions)
            board[row] = -1  # Backtrack

def main():
    # Validate command-line arguments
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

    # Initialize the board and solutions
    board = [-1] * n
    solutions = []

    # Solve the N-Queens problem
    solve_nqueens(n, 0, board, solutions)

    # Print solutions
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    main()
