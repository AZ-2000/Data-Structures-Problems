class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        else:
            seen = set()
            l,r = 0, 0
            maxlength = 0

            while r < len(s):
                if s[r] in seen:
                    length = r - l
                    maxlength = max(length,maxlength)

                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1
                seen.add(s[r])
                r += 1
            
            fin_length = r - l
            maxlength = max(maxlength, fin_length)
            return maxlength
                