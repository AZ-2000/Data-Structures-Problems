class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {")":"(","}":"{","]":"["}
        stack = []

        for c in s:
            if c in hashmap:
                if stack and hashmap[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        if not stack:
            return True
        else:
            return False