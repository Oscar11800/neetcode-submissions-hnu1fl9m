class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        l, r = 0, n*m-1
        mid = (l + r)//2

        row = mid // m
        col = mid % m

        while l <= r:
            if target == matrix[row][col]:
                return True
            elif target < matrix[row][col]:
                r = mid - 1
                mid = (l + r)//2
                row = mid // m
                col = mid % m
            else:
                l = mid + 1
                mid = (l + r)//2
                row = mid // m
                col = mid % m

        return False