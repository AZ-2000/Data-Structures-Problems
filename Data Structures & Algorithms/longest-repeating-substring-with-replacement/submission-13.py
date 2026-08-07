class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}

        l, r = 0, 0
        maxf = 0
        maxlength = 0
        while r < len(s):
            freq[s[r]] = 1 + freq.get(s[r],0)
            maxf = max(maxf,freq[s[r]])
            while (r-l+1) - maxf > k:
                freq[s[l]] -= 1
                l += 1
            maxlength = max(maxlength, r-l+1)
            r += 1
        maxlength = max(maxlength, r-l)
        return maxlength
            
