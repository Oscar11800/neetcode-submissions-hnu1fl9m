class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        queue = deque()
        pac, atl = set(), set()
        n, m = len(heights), len(heights[0])
        directions = [(1,0), (-1, 0), (0, 1), (0, -1)]

        # init pac
        for i in range(m):
            queue.append((0, i))
        for i in range(n):
            queue.append((i, 0))

        while queue:
            coord = queue.pop()
            pac.add(coord)
            for d in directions:
                new_row, new_col = coord[0] + d[0], coord[1] + d[1]
                new_coord = (new_row, new_col)
                if new_coord not in pac and 0 <= new_row < n and 0 <= new_col < m and heights[new_row][new_col] >= heights[coord[0]][coord[1]]:
                    queue.append(new_coord)

        # init atl
        for i in range(m):
            queue.append((n-1, i))
        for i in range(n):
            queue.append((i, m-1))

        while queue:
            coord = queue.pop()
            atl.add(coord)
            for d in directions:
                new_row, new_col = coord[0] + d[0], coord[1] + d[1]
                new_coord = (new_row, new_col)
                if new_coord not in atl and 0 <= new_row < n and 0 <= new_col < m and heights[new_row][new_col] >= heights[coord[0]][coord[1]]:
                    queue.append(new_coord)

        return [list(coord) for coord in pac & atl]