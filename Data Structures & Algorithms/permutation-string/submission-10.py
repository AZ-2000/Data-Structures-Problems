class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        else:
            s1count = {}
            s2count = {}

            for i in range(len(s1)):
                s1count[s1[i]] = 1 + s1count.get(s1[i],0) 
                s2count[s2[i]] = 1 + s2count.get(s2[i],0)
            
            if s1count == s2count:
                return True

            else:
                l = 0
                r = 0
                while r < len(s2):
                    if s2count == s1count:
                        return True
                    else:
                        s2count = {}
                        r = l + len(s1) 
                        new_str = s2[l: r]
                        l += 1
                        print(l, r, new_str)
                        if len(new_str) == len(s1):
                            for i in range(len(s1)):
                                s2count[new_str[i]] = 1 + s2count.get(new_str[i],0)
                        else:
                            return False
                    
                if s1count == s2count:
                    return True
                else:
                    return False



