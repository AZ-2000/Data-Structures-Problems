class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair_val = list(zip(position,speed))
        paired_list = [[item[0],item[1]] for item in pair_val]
        sorted_pair = sorted(paired_list, key=lambda x: x[0])
        print(sorted_pair)
        stack = []
        for p, s in sorted_pair:
            t = (target-p)/s
            if not stack:
                stack.append(t)
            else:
                while stack and t >= stack[-1]:
                    stack.pop()
                stack.append(t)
        return len(stack)   





        
