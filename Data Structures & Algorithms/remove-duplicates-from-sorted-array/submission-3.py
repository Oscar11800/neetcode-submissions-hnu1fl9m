class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write = 0
        for val in nums[1::]:
            if val == nums[write]:
                continue
            else:
                write += 1
                nums[write] = val
        return write+1