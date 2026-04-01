class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Return the number of distinct ways to climb n steps (1 or 2 steps at a time).

        :param n: Number of steps to the top.
        :return: Number of distinct ways to climb.
        """
        def climb(n, memo):
            if n in memo:
                return memo[n]
            if n <= 1:
                return 1
            memo[n] = climb(n-1, memo) + climb(n-2, memo)
            return memo[n]
        return climb(n, {})