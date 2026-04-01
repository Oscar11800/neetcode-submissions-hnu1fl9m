class Solution:
    def countSubstrings(self, s: str) -> int:
        rtn = 0
        n = len(s)

        for i in range(n):
            left = right = i
            while left >= 0 and right < n and s[left] == s[right]:
                rtn += 1
                left -= 1
                right += 1
            left = i
            right = i+1
            while left >= 0 and right < n and s[left] == s[right]:
                rtn += 1
                left -= 1
                right += 1

        return rtn