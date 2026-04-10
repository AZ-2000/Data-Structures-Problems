class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = [0] * 26
        for c in s:
            hashmap[ord(c) - ord('a')] += 1
        
        for c in t:
            hashmap[ord(c)-ord('a')] -= 1

        for i in hashmap:
            if i != 0:
                return False
        return True

            





