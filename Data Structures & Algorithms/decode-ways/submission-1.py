def decoder(s, index, cache):
    if index == len(s):
        return 1
    else:
        if cache[index] != -1:
            return cache[index]
        ways = 0
        if s[index] != '0':
            ways += decoder(s, index +1, cache)

        if index + 1 < len(s) and ( (s[index] == "1" and s[index+1] <= '9') or (s[index] == "2" and s[index+1] <= '6') ):
            
            ways += decoder(s, index + 2, cache)
        cache[index] = ways
        return ways


class Solution:
    def numDecodings(self, s: str) -> int:
        memo = [-1] * len(s)
        return decoder(s, 0, memo)
        