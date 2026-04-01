class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniques = set(nums)
        largest = 0

        while len(uniques) > 0:
            seq = 1
            og_curr = uniques.pop()
            curr = og_curr
            while curr - 1 in uniques:
                uniques.remove(curr-1)
                seq += 1
                curr -= 1
            curr = og_curr
            while curr + 1 in uniques:
                uniques.remove(curr+1)
                seq += 1
                curr += 1
            largest = max(largest, seq)
        return largest