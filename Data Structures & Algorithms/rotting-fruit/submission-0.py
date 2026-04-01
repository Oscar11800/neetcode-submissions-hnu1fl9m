class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        fresh_count = 0
        minutes = 0
        row_len, col_len = len(grid), len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        # initial fresh fruit count, setting rotten to queue
        for i in range(row_len):
            for j in range(col_len):
                if grid[i][j] == 1:
                    fresh_count += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))
        # edge case no fresh fruit
        if fresh_count == 0:
            return 0
        
        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for d in directions:
                    new_row, new_col = row + d[0], col + d[1]
                    if not 0 <= new_row < row_len or not 0 <= new_col < col_len or not grid[new_row][new_col] == 1:
                        continue
                    queue.append((new_row, new_col))
                    grid[new_row][new_col] = 2
                    fresh_count -= 1
            minutes += 1
            if fresh_count == 0:
                return minutes

        return -1