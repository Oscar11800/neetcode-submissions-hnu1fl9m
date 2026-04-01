class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_size = 0
        row_len, col_len = len(grid), len(grid[0])
        
        directions = [(1,0), (0, 1), (-1, 0), (0, -1)]

        def bfs(grid, row, col):
            queue = deque()
            grid[row][col] = 0
            queue.append((row, col))
            area = 1
            
            while queue:
                row, col = queue.popleft()
                for d in directions:
                    new_row = row + d[0]
                    new_col = col + d[1]
                    if not (0 <= new_row < row_len) or not (0 <= new_col < col_len) or grid[new_row][new_col] != 1:
                        continue
                    else:
                        area += 1
                        grid[new_row][new_col] = 0
                        queue.append((new_row, new_col))
            return area
            
        for i in range(row_len):
            for j in range(col_len):
                if grid[i][j] == 1:
                    area = bfs(grid, i, j)
                    max_size = max(area, max_size)
        return max_size