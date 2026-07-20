class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        d1 = {}
        for x in s:
            d1[x] = d1.get(x, 0) + 1

        d2 = {}
        for x in t:
            d2[x] = d2.get(x, 0) + 1
        
        return d1 == d2
        