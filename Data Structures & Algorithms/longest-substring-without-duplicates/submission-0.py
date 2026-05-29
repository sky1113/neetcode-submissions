class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        
        result = 1

        for l in range(len(s)):
            seen = {s[l]}
            curr_sum = 1

            for r in range(l + 1, len(s)):
                if s[r] not in seen:
                    seen.add(s[r])
                    curr_sum += 1

                else:
                    break
            
            result = max(result, curr_sum)
                        
        return result
            



