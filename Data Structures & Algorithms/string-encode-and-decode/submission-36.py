class Solution:

    def encode(self, strs: List[str]) -> str:
        delimiter = 0
        new_string = ""
        for s in strs:
            delimiter = str(len(s))
            new_string = new_string + delimiter + "#" + s
        return new_string

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j+1: j + length + 1])
            i = j + length + 1
        print(res)
        return res
        