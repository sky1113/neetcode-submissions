class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(lambda x: x.isalnum(), s))
        s = s.casefold()

        front = 0
        back = len(s) - 1
        while front <= back:
            front_char = s[front]
            back_char = s[back]
            if front_char != back_char:
                return False;
            front += 1
            back -= 1
        return True