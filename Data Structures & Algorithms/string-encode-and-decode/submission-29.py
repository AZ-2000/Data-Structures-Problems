class Solution:
    def encode(self, strs: List[str]) -> str:
        delimiter = 0
        res = []
        for s in strs:
            delimiter = len(s)
            s = str(len(s))+"#" + s
            res.append(s)
            
        s = ("").join(res)
        return s

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != "#":
                j+= 1
            length = int(s[i:j])
            res.append(s[j+1: length + j + 1])
            i = j + length + 1
        return res
        