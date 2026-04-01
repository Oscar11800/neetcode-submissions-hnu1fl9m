class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Sort nums in-place: reds (0), whites (1), blues (2).
        Do not return anything; modify nums in-place.
        """
        buckets = [0]*3
        for num in nums:
            buckets[num] += 1
        
        idx = 0
        for i in range(3):
            for n in range(buckets[i]):
                nums[idx] = i
                idx += 1