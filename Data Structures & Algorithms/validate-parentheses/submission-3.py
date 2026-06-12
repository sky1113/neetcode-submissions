class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        parens = {
            ")": "(",
            "}": "{",
            "]": "["
            }

        for i in s:
            if i in parens.values():
                stack.append(i)
            if i in parens.keys():
                if len(stack) == 0:
                    return False
                if stack[-1] != parens[i]:
                    return False
                if stack[-1] == parens[i]:
                    stack.pop()
            
        
        if len(stack) > 0:
            return False
        
        return True