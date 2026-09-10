class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxlength = 0
        res_string = ""
        for i in range(len(s)):
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            if (r-l) + 1 > maxlength:
                maxlength = (r-l) + 1
                res_string = s[l+1:r]
            l , r = i, i + 1
            length = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            if (r-l) + 1 > maxlength:
                maxlength = (r-l) + 1
                res_string = s[l+1:r]
        return res_string
