class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: 
            return 0
        dp = [1] * (len(nums))
        rtn = 0
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j] + 1, dp[i])
            rtn = max(dp[i], rtn)

        return rtn