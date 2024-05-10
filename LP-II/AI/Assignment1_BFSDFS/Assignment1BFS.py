from collections import deque


class Solution:
    def count_islands_BFS(self, matrix):
        if not matrix:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])
        totalIslands = 0

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 1:  
                    totalIslands += 1
                    self.visit_is_land_BFS(matrix, i, j)
                    print(f"Found Island: {totalIslands}")

        return totalIslands

    def visit_is_land_BFS(self, matrix, x, y):
        rows = len(matrix)
        cols = len(matrix[0])
        level = 0  
        neighbors = deque([(x, y, level)])  

        while neighbors:
            row, col, level = neighbors.popleft()

            if row < 0 or row >= rows or col < 0 or col >= cols:
                continue  
            if matrix[row][col] == 0:
                continue  

            matrix[row][col] = 0  

            print(f"Visiting cell ({row}, {col}) at level {level}")

            
            level += 1

            
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                neighbors.append((new_row, new_col, level))


def main():
    sol = Solution()

    
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    matrix = []
    print("Enter the matrix row by row (0 for water, 1 for land): ")
    for i in range(rows):
        row = list(map(int, input().split()))
        matrix.append(row)

    print("Number of islands:", sol.count_islands_BFS(matrix))


if __name__ == "__main__":
    main()
