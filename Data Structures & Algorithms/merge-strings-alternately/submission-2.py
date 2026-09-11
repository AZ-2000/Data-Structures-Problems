class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        ptr_1 = 0
        ptr_2 = 0

        for i in range(len(word1) + len(word2)):
            print(res)
            if ptr_2 == len(word2) or ptr_1 == len(word1):
                    break
            if i%2 == 0:
                res += word1[ptr_1]
                ptr_1 += 1
            else:
                res += word2[ptr_2]
                ptr_2 += 1
        if ptr_2 == len(word2):
            res += word1[ptr_1:len(word1)]
        elif ptr_1 == len(word1):
            res += word2[ptr_2:len(word2)]
        return res



