class Solution:

    def encode(self, strs: List[str]) -> str:
        empty = ""
        for c in strs:
            empty += str(len(c)) + "#" 
            empty += c

        return empty

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        else:
            left, right = 0, 0
            res = []
            num = ""
            while right < len(s):
                if s[right] != "#":
                    num += s[right]
                else:
                    num = int(num)
                    left = right + 1
                    right = num + left -1
                    new_str = s[left:right + 1]
                    res.append(new_str)
                    num = ""
                right += 1
            
            return res
        



                


