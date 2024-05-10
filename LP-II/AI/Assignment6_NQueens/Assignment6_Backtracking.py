def issafe(arr, x, y, n):
    for row in range(x):
        if arr[row][y] == "Q":
            # Checking column attack
            return False
    row = x
    col = y
    # Checking Diagonal Attack
    while row >= 0 and col >= 0:
        if arr[row][col] == "Q":
            return False
        row -= 1
        col -= 1

    row = x
    col = y
    # Checking Anti Diagonal Attack
    while row >= 0 and col < n:
        if arr[row][col] == "Q":
            return False
        row -= 1
        col += 1

    return True


def nQueen(arr, x, n):
    if x >= n:
        return True

    for col in range(n):
        if issafe(arr, x, col, n):
            arr[x][col] = "Q"
            if nQueen(arr, x + 1, n):
                return True
            arr[x][col] = "_"

    return False


def main():
    n = int(input("Enter number of Queens : "))
    arr = [["_"] * n for i in range(n)]

    if nQueen(arr, 0, n):
        for i in range(n):
            for j in range(n):
                print(arr[i][j], end=" ")
            print()


if __name__ == "__main__":
    main()
