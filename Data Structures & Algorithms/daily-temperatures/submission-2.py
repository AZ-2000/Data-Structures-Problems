class Solution:

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
       

        for i in range(len(temperatures)):
            if not stack:
                stack.append([temperatures[i],i])
            else:
                print(stack[-1])
                while stack and stack[-1][0] < temperatures[i]:
                    val, idx = stack.pop()
                    diff = i - idx
                    res[idx] = diff
                stack.append([temperatures[i],i])

        return res
            

