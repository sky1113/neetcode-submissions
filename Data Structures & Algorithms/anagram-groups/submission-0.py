class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        set_map = {}

        for string in strs:
            curr_set = tuple(sorted(string))
            if curr_set in set_map.keys():
                set_map[curr_set].append(string)
            else:
                set_map[curr_set] = [string]
        
        return list(set_map.values())