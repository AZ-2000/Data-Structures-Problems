class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {")":"(","}":"{","]":"["}
        stack = []
        for c in s:
            if stack and c in hashmap:
                if hashmap[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        if stack:
            return False
        else:
            return True