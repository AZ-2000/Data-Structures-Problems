class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {")":"(", "]":"[", "}":"{"}
        stack = []

        for i in range(len(s)):
            if s[i] in hashmap:
                if stack and stack[-1] == hashmap[s[i]]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])
            

        if stack:
            return False
        else:
            return True