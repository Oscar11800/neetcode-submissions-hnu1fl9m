class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        rtn = nums[0]
        max_product = 1
        min_product = 1
        for i in range(len(nums)):
            temp = max_product
            max_product = max(nums[i], nums[i] * max_product, nums[i] * min_product)
            min_product = min(nums[i], nums[i] * temp, nums[i] * min_product)
            rtn = max(max_product, rtn)

        return rtn