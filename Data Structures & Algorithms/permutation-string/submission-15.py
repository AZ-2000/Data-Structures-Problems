class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        else:
            s1count = {}
            s2count = {}
            l, r = 0, 0

            for i in range(len(s1)):
                s1count[s1[i]] = s1count.get(s1[i], 0) + 1
                s2count[s2[i]] = s2count.get(s2[i], 0) + 1
            
            if s2count == s1count:
                return True
            else:
                r = len(s1)
                while r < len(s2):
                    if s2count == s1count:
                        return True
                    else:
                        s2count[s2[l]] -= 1
                        if s2count[s2[l]] == 0:
                            del s2count[s2[l]]
                        l += 1
                        s2count[s2[r]] = s2count.get(s2[r],0) + 1
                        r += 1
                return s2count == s1count

