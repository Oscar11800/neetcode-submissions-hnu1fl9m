class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = Counter()
        max_count = 0
        left, right = 0, 0

        while right < len(s):
            freq.update(s[right])
            if (right - left + 1) - max(freq.values()) <= k:
                max_count = max((right-left + 1), max_count)
            else:
                freq.subtract(s[left])
                left += 1
            right += 1
        return max_count