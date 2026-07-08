class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        maxf = 0
        l, r = 0, 0
        while r < len(s):
            count[s[r]] = count.get(s[r], 0) + 1
            maxf = max(maxf, count[s[r]])
            while (r-l+1) - k > maxf:
                count[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
            r += 1
        return res






        

    