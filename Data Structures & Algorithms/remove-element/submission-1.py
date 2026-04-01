class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        lag = 0
        lead = 0
        length = len(nums)
        while(lead < length):
            if nums[lead] is not val:
                nums[lag] = nums[lead]
                lag += 1
            lead += 1
        return lag