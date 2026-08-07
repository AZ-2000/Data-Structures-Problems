class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l, r = 0,0
        maxlength = 0
        while r < len(s):
            maxlength = max(maxlength, r - l)

            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            r += 1
        maxlength = max(maxlength, r-l)
        return maxlength
