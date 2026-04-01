class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        rtn = []
        base = ord('a')
        matchmap = {}

        for s in strs:
            charmap = {i : 0 for i in range(26)}
            for c in s:
                charmap[ord(c) - base] += 1
            key = tuple(charmap.values())
            if key in matchmap:
                rtn[matchmap[key]].append(s)
            else:
                matchmap[key] = len(rtn)
                rtn.append([s])
        return rtn