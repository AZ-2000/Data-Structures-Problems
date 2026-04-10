class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict, t_dict = {},{}

        if len(s) != len(t):
            return False

        for c in s:
            if c in s_dict:
                s_dict[c] += 1
            else:
                s_dict[c] = 1
        
        for c in t:
            if c in t_dict:
                t_dict[c] += 1
            else:
                t_dict[c] = 1
        
        for key in s_dict:
            if key in t_dict and s_dict[key]==t_dict[key]:
                continue
            else:
                return False
        return True


