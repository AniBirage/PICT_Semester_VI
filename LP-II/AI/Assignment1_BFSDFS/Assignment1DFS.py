class Solution:
    def countIslands(self, matrix):
        if not matrix:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])
        totalIslands = 0

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 1:
                    totalIslands += 1
                    self.visit_is_land_DFS(matrix, i, j)
                    print("Found Island:", totalIslands)

        return totalIslands

    def visit_is_land_DFS(self, matrix, x, y, level=0):
        rows = len(matrix)
        cols = len(matrix[0])

        if x < 0 or x >= rows or y < 0 or y >= cols:
            return  
        if matrix[x][y] == 0:
            return  

        matrix[x][y] = 0

        print(f"Visiting cell ({x}, {y}) at level {level}")

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dx, dy in directions:
            self.visit_is_land_DFS(matrix, x + dx, y + dy, level + 1)


def main():
    sol = Solution()

    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    matrix = []
    print("Enter the matrix row by row (0 for water, 1 for land): ")
    for i in range(rows):
        row = list(map(int, input().split()))
        matrix.append(row)

    print("Number of islands:", sol.countIslands(matrix))


if __name__ == "__main__":
    main()
