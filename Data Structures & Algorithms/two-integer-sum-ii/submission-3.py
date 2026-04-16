class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1

        if not numbers:
            return 

        while left < right:
            summa = numbers[left] + numbers[right]
            if summa == target:
                return [left + 1, right + 1]
            elif summa < target:
                left += 1
            else:
                right -= 1
        

        