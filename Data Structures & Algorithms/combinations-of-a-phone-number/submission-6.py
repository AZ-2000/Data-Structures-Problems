def cartesian(idx, digits,res, curr, hashmap):
    if len(curr) == len(digits):
        res.append("".join(curr))
        return
    else:
        for i in range(idx, len(digits)):
            for j in range(0, len(hashmap[int(digits[i])])):
                curr.append(hashmap[int(digits[i])][j])
                cartesian(i+1, digits, res, curr, hashmap)
                curr.pop()        
        
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        hashmap = {2: "abc", 3:"def", 4:"ghi", 5:"jkl",6:"mno",
        7:"pqrs",8:"tuv",9:"wxyz"}

        res = []
        curr = []
        cartesian(0,digits, res, curr, hashmap)
        print(res)
        return res
        
        
        
        
        