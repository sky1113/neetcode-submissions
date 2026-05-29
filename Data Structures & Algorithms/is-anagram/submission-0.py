class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False;

        s_dict = {}
        t_dict = {}

        for i in range(len(s)):
            s_dict.update({s[i] : s.count(s[i])})
            t_dict.update({t[i] : t.count(t[i])})

        for k, v in s_dict.items():
            if t_dict.get(k) != v:
                return False
        return True
