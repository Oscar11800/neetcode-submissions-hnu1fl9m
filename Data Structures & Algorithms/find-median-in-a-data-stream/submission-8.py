class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap, -num)
        if self.min_heap and self.max_heap and -self.max_heap[0] >= self.min_heap[0]:
                heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        while len(self.max_heap) - len(self.min_heap) > 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
            # balance the tree
        while len(self.min_heap) - len(self.max_heap) > 1:
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        else:
            if len(self.max_heap) > len(self.min_heap):
                return -self.max_heap[0]
            else:
                return self.min_heap[0]
        
        