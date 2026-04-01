class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurences = defaultdict(int)
        # count occurences
        for num in nums:
            occurences[num] += 1
        heap = [(-val, key) for key, val in occurences.items()]
        heapq.heapify(heap)
        rtn = []

        for _ in range(k):
            rtn.append(heapq.heappop(heap)[1])
        return rtn