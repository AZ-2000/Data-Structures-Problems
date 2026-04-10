class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        right = len(numbers) - 1
        left = 0
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left+1, right+1]
            while sum < target:
                left += 1
                sum = numbers[left] + numbers[right]
            while sum > target:
                right -= 1
                sum = numbers[left] + numbers[right]
