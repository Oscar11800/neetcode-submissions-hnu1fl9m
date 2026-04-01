class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        rtn = []
        def dfs(nums: List[int], path: List[int], index: int) -> List[List[int]]:
            if index == len(nums):
                rtn.append(path)
                return
            dfs(nums, path, index + 1)
            dfs(nums, path + [nums[index]], index + 1)
            
        dfs(nums, [], 0)
        return rtn