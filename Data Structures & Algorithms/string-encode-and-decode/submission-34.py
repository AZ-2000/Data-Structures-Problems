class Solution:

    def encode(self, strs: List[str]) -> str:
        delimiter = 0
        new_string = ""
        for s in strs:
            delimiter = len(s)
            new_string = new_string+ str(delimiter)+"#"+ s
        return new_string

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            word = s[j+1:j+1+length]
            res.append(word)

            i = j + 1 + length
        return res

        




