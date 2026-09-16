from collections import deque as queue
def difference_calc(val1, val2):
    return abs(val1-val2)

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        l, r = 0, 0
        while r < len(arr):
            if arr[r] > x:
                break
            r += 1
        if r - k - 1 <= 0:
            l = 0
        else:
            l = r - k -1
        endpoint = r  + k
        r = endpoint 
        if r >= len(arr):
            r = len(arr)-1
        midpoint = (r+l) // 2
        print(midpoint,r,l)
        while (r-l+1) != k and r > 0:
            diff1 = difference_calc(arr[l], x)
            diff2 = difference_calc(arr[r], x)
            if diff1 > diff2:
                l += 1
            else:
                r -= 1 
        if l == r:
            if k == 1:
                return [arr[r]]
            else:
                r = midpoint + abs(k-l)-1
        return arr[l:r+1]