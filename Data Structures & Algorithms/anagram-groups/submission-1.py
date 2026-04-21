class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # if rtn empty then put the str into rtn, 
        # else check against each element of rtn's first element as a representative string
        # and check if it is an anagram
        # anagram check will be On and the checking against each is On so On^2 solution

        # we create an array of frequency maps and then for each str we change it to freq map
        # then we compare it to the array of freq maps. The comparisons are On and the 
        # creations are Om

        hashmap = {}
        rtn = []
        for s in strs:
            charmap = [0] * 26
            base = ord('a')

            for c in s:
                charmap[ord(c) - base] += 1

            key = tuple(charmap)

            if key in hashmap:
                rtn[hashmap[key]].append(s)
            else:
                hashmap[key] = len(rtn)
                rtn.append([s])

        return rtn