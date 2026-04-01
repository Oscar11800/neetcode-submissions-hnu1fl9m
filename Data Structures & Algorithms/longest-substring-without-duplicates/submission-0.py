class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        if len(s) == 1:
            return 1
        n = len(s)
        max_count = 1
        count = 1
        seen = set()
        left, right = 0, 1
        seen.add(s[left])
        while right < n:
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
                count -= 1
            seen.add(s[right])
            right += 1
            count += 1
            max_count = max(count, max_count)
        return max_count 