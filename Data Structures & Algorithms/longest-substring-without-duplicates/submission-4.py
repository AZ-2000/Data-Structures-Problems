class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left, right = 0,0
        count = 0
        maxCount = 0 
        while right < len(s):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
                count -= 1
            
            seen.add(s[right])
            count += 1

            maxCount = max(maxCount, count)
            right += 1
        return maxCount



