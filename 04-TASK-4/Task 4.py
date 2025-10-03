def PrintBoard(Board):
    for row in Board:
        print(" ".join(row))
    print("\n"+ "-" * (len(Board) * 2)) 

def Safe(Board, row, col, num):
    for x in range(row):
        if Board[x][col] == "Q":
            return False

    x, y = row - 1, col - 1
    while x >= 0 and y >= 0:
        if Board[x][y] == "Q":
            return False
        x -= 1
        y -= 1

    x, y = row - 1, col + 1
    while x >= 0 and y < num:
        if Board[x][y] == "Q":
            return False
        x -= 1
        y += 1

    return True

def Solve(Board, row, num):
    if row == num:
        PrintBoard(Board)
        return
    for col in range(num):
        if Safe(Board, row, col, num):
            Board[row][col] = "Q"
            Solve(Board, row + 1, num)
            Board[row][col] = "."


def NQueens(num):
    Board = [["."] * num for _ in range(num)]
    Solve(Board, 0, num)

NQueens(4)
