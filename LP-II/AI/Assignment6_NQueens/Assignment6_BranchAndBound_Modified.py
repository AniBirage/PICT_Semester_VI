class NQueens:
    def solve(self, row, n, board, column, left_diagonal, right_diagonal, result):
        if row == n:
            result.append([row[:] for row in board])
            return True  # Indicate that a solution is found

        for col in range(n):
            if not column[col] and not left_diagonal[row + col] and not right_diagonal[n - 1 + col - row]:
                board[row][col] = "Q"
                column[col] = True
                left_diagonal[row + col] = True
                right_diagonal[n - 1 + col - row] = True

                # Check if a solution is found
                if self.solve(row + 1, n, board, column, left_diagonal, right_diagonal, result):
                    return True

                board[row][col] = "_"
                column[col] = False
                left_diagonal[row + col] = False
                right_diagonal[n - 1 + col - row] = False

        return False  # Indicate that no solution is found

    def branch_and_bound(self, n):
        result = []

        left_diagonal = [False] * (2 * n - 1)
        right_diagonal = [False] * (2 * n - 1)
        column = [False] * n

        board = [["_"] * n for _ in range(n)]

        self.solve(0, n, board, column, left_diagonal, right_diagonal, result)

        return result

def main():
    n = int(input("Enter the Number of Queens: "))
    obj = NQueens()
    result = obj.branch_and_bound(n)

    if result:
        solution = result[0]  # Get the first solution
        for row in solution:
            print(" ".join(map(str, row)))
        print()
    
if __name__ == "__main__":
    main()
