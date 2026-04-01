class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = list(map(lambda s: -s, stones))
        heapq.heapify(stones)
        while len(stones) >= 2:
            s1 = heapq.heappop(stones)
            s2 = heapq.heappop(stones)
            diff = s2 - s1
            if diff != 0:
                heapq.heappush(stones, -diff)
        if len(stones):
            return -stones[0]
        else:
            return 0