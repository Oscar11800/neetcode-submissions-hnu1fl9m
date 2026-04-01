class Solution:
    def rob(self, nums: List[int]) -> int:
        best_sum = {}
        n = len(nums)
        def dfs(index):
            if index >= n:
                return 0
            if index in best_sum:
                return best_sum[index]
            else:
                best_sum[index] = max(dfs(index + 1), nums[index] + dfs(index + 2))
            return best_sum[index]
        return dfs(0)