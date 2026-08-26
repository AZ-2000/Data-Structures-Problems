def cart_prod(digits,ls, res, curr, row):
    if row == len(ls):
        res.append("".join(curr))
        return 
    else:
        for c in range(len(ls[row])):
            curr.append(ls[row][c])
            cart_prod(digits, ls, res, curr, row+1)
            curr.pop()
    
        
        
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        hashmap = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }
        res = []
        ls = []
        for d in digits:
            ls.append(hashmap[int(d)])
        cart_prod(digits,ls, res, [], 0)
        return res




        
        
        
        
        