class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {")":"(","]":"[","}":"{"}

        if s == "":
            return False
        
        for c in s:
            if c in hashmap:
                if stack and hashmap[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        if stack:
            return False
        else:
            return True