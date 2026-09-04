class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] *len(temperatures)
        stack = []
        for i in range(len(temperatures)-1,-1,-1):
            while stack and temperatures[i] >= stack[-1][1]:
                stack.pop()
            if stack and stack[-1][1] > temperatures[i]:
                idx = stack[-1][0]
                res[i] = idx - i
            
            stack.append([i, temperatures[i]])

        return res

