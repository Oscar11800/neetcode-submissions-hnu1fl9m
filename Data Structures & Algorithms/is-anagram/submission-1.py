class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # one solution is to sort both strings and compare which is Onlogn 
        # another solution is to have 2 hashmaps (counters) and have them count each and then
        # compare frequencies, this is On solution but also On storage as opposed to O1 space

        count1 = Counter(s)
        count2 = Counter(t)
        return count1 == count2