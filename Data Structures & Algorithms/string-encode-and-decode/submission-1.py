class Solution:

    def encode(self, strs: List[str]) -> str:
        """
        Encode list of strings into one string.

        :param strs: List of strings.
        :return: Encoded string.
        """
        encoded = ""
        if len(strs) == 0:
            return encoded
        for s in strs:
            s_str = "[" + str(len(s)) + "]" + s
            encoded += s_str
        return encoded

    def decode(self, s: str) -> List[str]:
        """
        Decode encoded string back into list of strings.

        :param s: Encoded string.
        :return: Original list of strings.
        """
        rtn = []
        i = 1
        while i < len(s):
            s_len = ""
            while s[i] != ']':
                s_len += s[i]
                i += 1
            s_len = int(s_len)
            i+= 1
            new_s = ""
            for i in range(i, i + s_len):
                new_s += s[i]
            rtn.append(new_s)
            if s_len > 0:
                i+= 2
            else:
                i += 1
        return rtn