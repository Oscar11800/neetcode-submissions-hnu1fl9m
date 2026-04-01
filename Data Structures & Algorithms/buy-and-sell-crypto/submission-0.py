class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        n = len(prices)
        left, right = 0, 1
        while right < n:
            if prices[right] < prices[left]:
                left = right
            else:
                max_profit = max(prices[right] - prices[left], max_profit)
            right += 1
        return max_profit