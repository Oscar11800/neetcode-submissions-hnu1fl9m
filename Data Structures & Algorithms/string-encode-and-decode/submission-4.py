class Solution:

    def encode(self, strs: List[str]) -> str:
        rtn = ""
        for s in strs:
            rtn += s
            rtn += '™'
        return rtn

    def decode(self, s: str) -> List[str]:
        rtn = []
        count = 0
        appendme = ""
        while count < len(s):
            current = s[count]
            if current == '™':
                rtn.append(appendme)
                appendme = ""
            else:
                appendme += current
            count += 1
        return rtn
