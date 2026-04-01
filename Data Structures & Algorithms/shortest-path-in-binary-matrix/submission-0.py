class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        row_len, col_len = len(grid), len(grid[0])
        queue = deque()
        visited = set()
        queue.append((0,0))
        visited.add((0, 0))
        length = 1
        directions = [(1,0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                if row == row_len - 1 and col == col_len - 1:
                    return length
                for direction in directions:
                    new_row, new_col = row + direction[0], col + direction[1]
                    if not 0 <= new_row < row_len or not 0 <= new_col < col_len or grid[new_row][new_col] != 0 or (new_row, new_col) in visited:
                        continue
                    visited.add((new_row, new_col))
                    queue.append((new_row, new_col))
            length += 1

        
        return -1