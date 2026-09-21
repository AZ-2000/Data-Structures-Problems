class Solution:
    def longestPalindrome(self, s: str) -> str:
        res_string = ""
        max_len = 0
        for i in range(len(s)):
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            if (r-l)+1 > max_len:
                max_len = (r-l) + 1
                res_string = s[l+1:r]
            l,r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            if (r-l) + 1 > max_len:
                max_len = (r-l) + 1
                res_string = s[l+1:r]
        return res_string
                
        
        