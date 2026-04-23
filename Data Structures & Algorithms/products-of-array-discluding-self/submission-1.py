class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # right and left products that moves
        # at i = 0, leftprod = 1, rightprod = nums[n] * nums[n-1] * ... * nums[1]
        # at i = 1, leftprod = nums[0], rightprod = nums[n] * nums[n-1] * ... * nums[2]
        # right and left avoid i

        # this is O(n) for left prod and O(n) for right prod and then final formulation is O(n)

        leftprod = []
        rightprod = []

        for i in range(len(nums)):
            if i == 0:
                leftprod.append(1)
            else:
                leftprod.append(leftprod[i-1] * nums[i-1])
        
        for i in range(len(nums)-1, -1, -1):
            print(i)
            if i == (len(nums)-1):
                rightprod.append(1)
            else:
                rightprod.append(rightprod[-1] * nums[i+1])
        rtn = []

        for i in range(len(nums)):
            rtn.append(leftprod[i] * rightprod[len(nums) - i - 1])

        return rtn