def cart_prod(digits,ls, res, curr, col, row, seen):
    if len(curr) == len(digits):
        if tuple(curr) in seen:
            return
        else:
            seen.add(tuple(curr))
            res.append("".join(curr))
        return
    if not (0<=row<len(ls)):
        return
    for c in range(len(ls[row])):
        curr.append(ls[row][c])
        cart_prod(digits, ls, res, curr, c, row+1, seen)
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
        seen = set()
        for d in digits:
            ls.append(hashmap[int(d)])

        for c in range(len(ls[0])):
            cart_prod(digits, ls,res,[], c, 0, seen)

        return res




        
        
        
        
        