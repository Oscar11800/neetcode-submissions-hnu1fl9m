class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        dp[n] = 1
        for i in range(n-1, -1, -1):
            ways = 0
            if 1 <= int(s[i]) <= 9:
                ways += dp[i+1]
            if i + 1 < n and 10 <= int(s[i:i+2]) <= 26:
                ways += dp[i+2]
            dp[i] = ways
        return dp[0]