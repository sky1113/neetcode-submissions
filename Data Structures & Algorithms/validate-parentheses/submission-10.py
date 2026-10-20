class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {
            ")":"(",
            "]":"[",
            "}":"{"
        }

        stack = []
        for paren in s:
            if paren in closeToOpen.values():
                stack.append(paren)
            elif paren in closeToOpen.keys():
                if not stack or stack[-1] != closeToOpen[paren]:
                    return False
                else:
                    stack.pop()
        return not stack