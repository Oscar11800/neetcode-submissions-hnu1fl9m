class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        og_color = image[sr][sc]
        if color == og_color:
            return image
        row_length = len(image)
        col_length = len(image[0])
        def dfs(r, c):
            if r < 0 or r >= row_length or c < 0 or c >= col_length or image[r][c] != og_color:
                return image
            image[r][c] = color
            dfs(r + 1, c)
            dfs(r, c + 1)
            dfs(r - 1, c)
            dfs(r, c - 1)
            
        dfs(sr, sc)
        return image