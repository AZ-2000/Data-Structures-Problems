class Solution:

    def encode(self, strs: List[str]) -> str:
        delimiter = 0
        new_string = ""
        for s in strs:
            delimiter = len(s)
            new_string =new_string+ str(len(s))+"#" + s
        print(new_string)
        return new_string


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        word = ""
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j+1:length+j+1])
            i = j + length + 1
        return res




