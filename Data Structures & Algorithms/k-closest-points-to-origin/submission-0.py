class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        rtn = []
        min_heap = list(map(lambda point: (point[0] ** 2 + point[1] ** 2, point), points))
        heapq.heapify(min_heap)
        for _ in range(k):
            rtn.append(heapq.heappop(min_heap)[1])
        return rtn