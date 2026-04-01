class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        """
        Initialize with k and initial stream nums.
        """
        self.k = k
        self.nums = []
        for num in nums:
            if len(self.nums) == k:
                if num > self.nums[0]:
                    heapq.heappop(self.nums)
                    heapq.heappush(self.nums, num)
            else:
                heapq.heappush(self.nums, num)

    def add(self, val: int) -> int:
        """
        Add val to the stream and return the kth largest integer.
        """
        if len(self.nums) == self.k:
            if val >= self.nums[0]:
                heapq.heappop(self.nums)
                heapq.heappush(self.nums, val)
        else:
            heapq.heappush(self.nums, val)
        return self.nums[0]
