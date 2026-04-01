class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(1,0), (-1, 0), (0, 1), (0, -1)]
        n, m = len(board), len(board[0])
        def dfs(cell: tuple[int], index: int) -> bool:
            if index == len(word):
                return True
            r, c = cell
            if not 0 <= r < n or not 0 <= c < m or word[index] != board[r][c]:
                return False
            # found char
            if index + 1 == len(word):
                return True
            board[r][c] = '#'
            for d in directions:
                new_r, new_c = r + d[0], c + d[1]
                if 0 <= new_r < n and 0 <= new_c < m and board[new_r][new_c] != '#':
                    if dfs((new_r, new_c), index + 1):
                        return True
                        
            board[r][c] = word[index]
            return False
        for i in range(n):
            for j in range(m):
                if dfs([i,j], 0):
                    return True

        return False