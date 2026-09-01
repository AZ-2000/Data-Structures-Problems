class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_val = arr[len(arr)-1]
        for i in range(len(arr)-1, -1,-1):
            if i == len(arr)-1:
                arr[i] = -1
                continue
            else:
                tmp = max_val
                max_val = max(arr[i],max_val)
                arr[i] = tmp
        return arr

        