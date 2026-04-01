class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        rtn = ""
        for i in range(n):
            left = right = i
            righteven = i + 1
            while right <= n-1 and left >= 0 and s[right] == s[left]:
                if (right - left + 1) > len(rtn):
                    rtn = s[left:right+1]
                left -= 1
                right += 1
            left = i
            while righteven <= n-1 and left >= 0 and s[righteven] == s[left]:
                if (righteven - left + 1) > len(rtn):
                    rtn = s[left:righteven+1]
                left -= 1
                righteven += 1
        return rtn