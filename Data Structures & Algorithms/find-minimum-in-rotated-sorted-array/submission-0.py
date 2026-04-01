class Solution:
    def findMin(self, nums: List[int]) -> int:
        minimum = nums[0]
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            minimum = min(minimum, nums[mid])
            if nums[left] <= nums[mid]:
                if nums[left] < nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[right] > nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        return minimum