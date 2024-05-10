class NQueens:
    def solve(self, row, n, board, column, left_diagonal, right_diagonal, result):
        if row == n:
            result.append([row[:] for row in board])
            return

        for col in range(n):
            if not column[col] and not left_diagonal[row + col] and not right_diagonal[n - 1 + col - row]:
                board[row][col] = 1
                column[col] = True
                left_diagonal[row + col] = True
                right_diagonal[n - 1 + col - row] = True

                self.solve(row + 1, n, board, column, left_diagonal, right_diagonal, result)

                board[row][col] = 0
                column[col] = False
                left_diagonal[row + col] = False
                right_diagonal[n - 1 + col - row] = False

    def branch_and_bound(self, n):
        result = []

        left_diagonal = [False] * (2 * n - 1)
        right_diagonal = [False] * (2 * n - 1)
        column = [False] * n

        board = [[0] * n for _ in range(n)]

        self.solve(0, n, board, column, left_diagonal, right_diagonal, result)

        return result


def main():
    n = int(input("Enter the Number of Queens:"))
    obj = NQueens()

    result = obj.branch_and_bound(n)

    print(f"\n N Queens Puzzle Solutions by Branch and Bound & Backtracking for N = {n}\n")
    for i, solution in enumerate(result):
        print(f"----- Solution {i + 1} -----")
        for row in solution:
            print(" ".join(map(str, row)))
        print()

    print("Thank you for using the program.\n")


if __name__ == "__main__":
    main()
