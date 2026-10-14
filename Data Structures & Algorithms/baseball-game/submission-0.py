class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for n in operations:
            if n not in ["+", "C", "D"]:
                stack.append(int(n))
            elif n == "+":
                stack.append(stack[-1] + stack [-2])
            elif n == "D":
                stack.append(stack[-1] * 2)
            elif n == "C":
                stack.pop()
        
        res = 0
        for n in stack:
            res += n
        
        return res