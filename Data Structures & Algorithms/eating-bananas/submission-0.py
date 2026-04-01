class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        while left < right:
          mid = (left + right)//2
          totalh = sum(map(lambda x: math.ceil(x/mid), piles))
          if totalh > h:
            left = mid + 1
          else:
            right = mid

        return left