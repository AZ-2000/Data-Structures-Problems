class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        min_len = min(strs, key = len)
        i = 0
        for item in strs:
            for c in item:
                if i >= len(min_len):
                    break
                else:
                    if c == min_len[i]:
                        i = i + 1
                        continue
                    else:
                        min_len = min_len[:i]
                        break
            i = 0
        return min_len