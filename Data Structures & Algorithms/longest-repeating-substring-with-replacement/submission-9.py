class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        r, l = 0, 0
        maxf = 0
        maxlength = 0

        while r < len(s):
            count[s[r]] = count.get(s[r], 0) + 1
            maxf = max(maxf, count[s[r]])
            while (r-l + 1) - k > maxf:
                count[s[l]] -= 1
                l += 1
            maxlength = max(r-l + 1 ,maxlength)  
            r += 1
        return maxlength
  





        

    