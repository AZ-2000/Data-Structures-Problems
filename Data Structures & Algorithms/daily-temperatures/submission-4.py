class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures) 
        length = 0
        for i in range(len(temperatures)-1,-1,-1):
            while stack and temperatures[i] >= stack[-1][0]:
                print(stack)
                stack.pop()
            if not stack:
                res[i] = 0
                stack.append((temperatures[i],i))
            else:
                res[i] = stack[-1][1] - i
                stack.append((temperatures[i],i))
        return res
                


                





        