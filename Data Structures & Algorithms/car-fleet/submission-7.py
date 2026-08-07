class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:       
        #time = distance/speed
        #sort the pair of position and speed first

        cars = sorted(zip(position, speed))

        stack = []
        for p, s in reversed(cars):
            time = (target-p)/s
            # print(stack)
            if not stack or time > stack[-1]:
                stack.append(time)
                

        return len(stack)




