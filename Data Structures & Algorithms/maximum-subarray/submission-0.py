class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        rtn = float('-inf')
        curr_sum = 0
        for num in nums:
            curr_sum += num
            rtn = max(curr_sum, rtn)
            if curr_sum < 0:
                curr_sum = 0
        return rtn