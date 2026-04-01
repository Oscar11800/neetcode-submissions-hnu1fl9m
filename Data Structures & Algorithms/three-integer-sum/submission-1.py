class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        rtn = []
        targetmap = {}
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                target = -(nums[i] + nums[j])
                targetmap.setdefault(target, []).append((i, j))
        for idx, num in enumerate(nums):
            if num not in targetmap:
                continue
            for (i, j) in targetmap[num]:
                if idx != i and idx != j:
                    rtn.append([nums[i], nums[j], nums[idx]])
        return [list(t) for t in {tuple(sorted(x)) for x in rtn}]