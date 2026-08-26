def cart_prod(digits, ls, row, curr, res):
    if len(curr) == len(digits):
        res.append("".join(curr))
        return
    
    for c in range(len(ls[row])):
        curr.append(ls[row][c])
        cart_prod(digits, ls, row+1, curr, res)
        curr.pop()
        
        
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        hashmap = {
            2:"abc",
            3: "def",
            4: "ghi",
            5:"jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }

        ls = []
        res = []
        for item in digits:
            ls.append(hashmap[int(item)])
        cart_prod(digits, ls, 0, [], res)
        return res
        
        
        
        
        