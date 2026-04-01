class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(remaining, path, index):
            if remaining == 0:
                res.append(path[:])
                return res
            elif remaining < 0:
                return
            if index >= len(nums) and remaining > 0:
                return
            dfs(remaining, path, index + 1)
            dfs(remaining - nums[index], path + [nums[index]], index)
        dfs(target, [], 0)
        return res