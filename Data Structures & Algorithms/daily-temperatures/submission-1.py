class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        mon_stack = [] # pair: (temp, index)
        res = [0] * len(temperatures) 

        for i, t in enumerate(temperatures):
            while mon_stack and t > mon_stack[-1][0]:
                stackT, stackInd = mon_stack.pop()
                res[stackInd] = i - stackInd
            mon_stack.append([t,i])
        return res
            