class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freqMap = {}

        for i in strs:
            freq = [0] * 26

            for j in i:
                freq[ord(j) - ord('a')] += 1
            
            if tuple(freq) in freqMap.keys():
                freqMap[tuple(freq)].append(i)
            else:
                freqMap[tuple(freq)] = [i]

        groups = []

        for x in freqMap:
            groups.append(freqMap[x])

        return groups

            
