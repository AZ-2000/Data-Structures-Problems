class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            alive = True
            while stack and ast < 0 and stack[-1] > 0:
                diff = stack[-1] + ast 
                if diff > 0:
                    alive = False
                    break
                elif diff < 0:
                    stack.pop()
                elif diff == 0:
                    alive = False
                    stack.pop()
                    break
            if alive:
                stack.append(ast)
                
        return stack


        



        
        