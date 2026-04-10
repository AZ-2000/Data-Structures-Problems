class Solution:
    def encode(self, strs: List[str]) -> str:
        delimiter = 0
        tmp = ""
        for s in strs:
            delimiter = len(s)
            tmp += str(delimiter) + "#" + s
        return tmp

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j+1 : j + 1 + length])
            i = j + length + 1
        return res