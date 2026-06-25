class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        l,r=0,0
        maxlen = 0
        seen = set()
        while r < len(s):
            if s[r] in seen:
                length = r-l 
                print(length, l, r)
                maxlen = max(maxlen, length)
                while s[r] in seen:
                    seen.remove(s[l])
                    l+=1 
            seen.add(s[r])
            r += 1
        
        fin_length = r-l
        print(r,l)
        maxlen = max(maxlen,fin_length)
        
    
        return maxlen
            
            
        