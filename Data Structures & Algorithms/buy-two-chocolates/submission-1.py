class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        first, second, = float('infinity'), float('infinity')
        for i in range(len(prices)):
            if prices[i] <= first:
                second = first
                first = prices[i]
            elif prices[i] < second and prices[i] != first:
                second = prices[i]
        if first + second > money:
            return money
        else:
            return ((money) - (first+second))

        