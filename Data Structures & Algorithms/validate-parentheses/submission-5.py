class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {"}":"{", ")":"(","]":"["}
        stack = []

        for c in s:
            if not stack:
                stack.append(c)
            else:
                if c in hashmap and hashmap[c] == stack[-1]:
                    stack.pop()
                else:
                    stack.append(c)

        print(stack)
        if not stack:
            return True
        else:
            return False
