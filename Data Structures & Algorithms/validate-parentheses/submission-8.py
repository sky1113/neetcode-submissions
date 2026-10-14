class Solution:
    def isValid(self, s: str) -> bool:
        parens = {
            ")":"(",
            "}":"{",
            "]":"["    
        }

        stack = []

        for paren in s:
            if paren in parens.values():
                stack.append(paren)
            elif paren in parens.keys():
                if stack and stack[-1] == parens[paren]:
                    stack.pop()
                else:
                    return False
        
        return not stack