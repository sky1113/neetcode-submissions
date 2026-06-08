class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sMap = {}
        tMap = {}

        for i in s:
            if i in sMap.keys():
                sMap[i] += 1
            else:
                sMap[i] = 1

        for i in t:
            if i in tMap.keys():
                tMap[i] += 1
            else:
                tMap[i] = 1
        
        return sMap == tMap
        