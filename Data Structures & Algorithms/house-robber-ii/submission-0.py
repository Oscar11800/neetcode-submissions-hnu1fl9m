class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        dp1 = [None] * (n-1)
        dp2 = [None] * (n-1)

        def dfs(house, dp, arr):
            if house >= (n-1):
                return 0
            if dp[house] != None:
                return dp[house]
            else:
                dp[house] = max(arr[house] + dfs(house+2, dp, arr), dfs(house+1, dp, arr))
            return dp[house]

        return max(dfs(0, dp1, nums[1:]), dfs(0, dp2, nums[:-1]))