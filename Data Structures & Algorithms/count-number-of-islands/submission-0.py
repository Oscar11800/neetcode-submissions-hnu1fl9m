class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        counter = 2
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        row_len, col_len = len(grid), len(grid[0])

        def dfs(grid, row, col, counter):
            if 0 <= row < row_len and 0 <= col < col_len and grid[row][col] == "1":
                grid[row][col] = counter
            else:
                return
            for d in directions:
                dfs(grid, row + d[0], col + d[1], counter)
        
        
        for i in range(row_len):
            for j in range(col_len):
                if grid[i][j] == "1":
                    dfs(grid, i, j, counter)
                    counter += 1
        return counter - 2