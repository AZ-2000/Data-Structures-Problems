def cartesian(idx, digits,res, curr, hashmap):
    if idx == len(digits):
        res.append("".join(curr))
        return
    else:
        for j in range(len(hashmap[int(digits[idx])])):
            curr.append(hashmap[int(digits[idx])][j])
            cartesian(idx+1, digits, res, curr, hashmap)
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
        
        
        
        
        