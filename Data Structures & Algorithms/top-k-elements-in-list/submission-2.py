class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create hashmap of counts O(n)
        # sort the keys based on their values O(nlogn)
        # return the first k keys O(k)

        counts = Counter(nums)
        sorted_counts = tuple(sorted(counts.items(), key=lambda item: item[1], reverse=True))
        rtn = []

        for i in range(k):
            rtn.append(sorted_counts[i][0])

        return rtn
