class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        strings = []
        l, r = 0, 0
        freq = {}
        seen = set()
        for c in s:
            freq[c] = 1 + freq.get(c, 0)
        
        while r < len(s):
            seen.add(s[r])
            freq[s[r]] -= 1
            count = 0
            for c in seen:
                if freq[c] == 0:
                    count += 1
            if count == len(seen):
                seen = set()
                res.append(r-l+1)
                # strings.append(s[l:r+1])
                l = r + 1

            r += 1
        # print(strings)
        return res
                


