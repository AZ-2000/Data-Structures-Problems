class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(B) < len(A):
            A,B = B,A
        
        l, r = 0, len(A)-1
        total = len(B) + len(A)
        half = total//2

        while True:
            i = (l+r)//2
            j = half - i - 2 #to accomodate zero indexing in arrays
            Aendleft = A[i] if i >= 0 else float("-infinity")
            Astartright = A[i+1] if i + 1 < len(A) else float("infinity")
            Bendleft = B[j] if j >= 0 else float("-infinity")
            Bstartright = B[j+1] if j + 1 < len(B) else float("infinity")
            
            if Aendleft <= Bstartright and Astartright >= Bendleft:
                if total % 2:
                    return min(Astartright, Bstartright)
                else:                    
                    return (max(Aendleft, Bendleft) + min(Astartright, Bstartright))/2
            elif Aendleft > Bstartright:
                r = i - 1
            else: #if Bendleft > Astartright
                l = i + 1
            


        

        
        