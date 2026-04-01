class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == "" or t == "":
            return ""
        if len(s) < len(t):
            return ""

        freqt = Counter(t)
        window = Counter()

        have = 0
        need = len(freqt)

        left, right = 0, 0
        n = len(s)
        rtn_str = ""

        for right in range(n):
            if s[right] in freqt.keys():
                window[s[right]] += 1
                if window[s[right]] == freqt[s[right]]:
                    have += 1
            while have == need:
                if (right - left + 1) < len(rtn_str) or rtn_str == "":
                    rtn_str = s[left:right+1]
                if s[left] in freqt.keys():
                    window.subtract(s[left])
                    if window[s[left]] < freqt[s[left]]:
                        have -= 1
                left += 1
        return rtn_str