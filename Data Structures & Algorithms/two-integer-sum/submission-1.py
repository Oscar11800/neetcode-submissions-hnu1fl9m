class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # have a hashmap mapping the in with the indices
        hashmap = {}
        for index, value in enumerate(nums):
            diff = target - value
            if diff in hashmap:
                return [hashmap.get(diff), index]
            else:
                hashmap[value] = index
                print(hashmap)
        return []
        