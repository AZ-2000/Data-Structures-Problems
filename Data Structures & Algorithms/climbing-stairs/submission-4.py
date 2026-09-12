class Solution:
    def climbStairs(self, n: int) -> int:
        onestep, twosteps = 1, 1
        for i in range(2, n+1):
            tmp = onestep + twosteps
            twosteps = onestep
            onestep = tmp
        return onestep

            
            

        
        