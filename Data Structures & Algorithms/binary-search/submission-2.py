class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """
        Binary search for target in sorted nums.

        :param nums: Sorted array of distinct integers.
        :param target: Value to search for.
        :return: Index of target, or -1 if not found.
        """
        l, r = 0, len(nums)-1
        m = math.ceil((l+r)/2)

        while l <= r:
            if nums[m] == target:
                return m
            elif target < nums[m]:
                r = m - 1
                m = math.ceil((l+r)/2)
            else:
                l = m + 1
                m = math.ceil((l+r)/2)
        return -1