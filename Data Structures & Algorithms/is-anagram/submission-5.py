class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen_1 = {}
        seen_2 = {}
        if len(s) != len(t):
            return False

        else:
            for i in range(len(s)):
                if s[i] not in seen_1:
                    seen_1[s[i]] = 0
                else:
                    seen_1[s[i]] += 1
            for i in range(len(t)):
                if t[i] not in seen_1:
                    return False
                else:
                    if t[i] not in seen_2:
                        seen_2[t[i]]=0
                    else:
                        seen_2[t[i]] += 1
            if seen_1 != seen_2:
                return False
            else:
                return True