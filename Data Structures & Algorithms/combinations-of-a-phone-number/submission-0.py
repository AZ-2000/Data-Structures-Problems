def helper(idx, ls,res, curr):
    if idx == len(ls):
        res.append("".join(curr))
        return
    if not ls:
        return
    for item in ls[idx]:
        curr.append(item)
        helper(idx + 1,ls,res, curr)
        curr.pop()


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        hashmap ={
            2:['a','b','c'],
            3: ['d','e','f'],
            4: ['g','h','i'],
            5: ['j','k','l'],
            6: ['m','n','o'],
            7:['p','q','r','s'],
            8: ['t','u','v'],
            9: ['w','x','y','z']
        }

        dig = list(digits)
        ls_ls = []
        for i in range(len(dig)):
            dig[i] = int(dig[i])
            ls_ls.append(hashmap[dig[i]])
        res = []
        helper(0, ls_ls, res, [])
        return res
        
        
        
        
        