boardExample = [
    [0, 4, 0, 0, 0, 3, 0, 5, 0],
    [0, 0, 7, 0, 0, 1, 0, 6, 4],
    [0, 0, 9, 0, 5, 0, 0, 8, 0],
    [7, 5, 0, 6, 0, 0, 0, 0, 0],
    [6, 0, 1, 4, 0, 0, 3, 0, 0],
    [0, 9, 3, 0, 0, 0, 0, 0, 0],
    [3, 0, 0, 0, 7, 0, 0, 0, 0],
    [0, 0, 5, 0, 8, 0, 0, 0, 6],
    [0, 8, 0, 0, 0, 0, 0, 0, 0]
]


# Backtracking algorithm which solves the board recursively
def solve(board):

    #print_board(board)
    #print("")

    # Base Case
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    # Looping through values 1 through 9 to plug into the empty board space
    for i in range(1, 10):
        if valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    # If we looped through all numbers and none returned a valid solution
    return False


# Function which prints the sudoku board in text format
def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


# Function which finds the first empty square in the board
def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  # i = row, j = col

    return None


# Function which checks if a given number within a board space is valid
def valid(board, num, pos):
    # Check the row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check the column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Create the positions of each box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    # Check the box
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True

print("Base Board:")
print("")
print_board(boardExample)
print("")
solve(boardExample)
print("Solved Board:")
print("")
print_board(boardExample)
