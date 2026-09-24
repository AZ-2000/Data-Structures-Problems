class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five_dollar_count = 0
        ten_dollar_count = 0

        for bill in bills:
            if bill == 5:
                five_dollar_count += 1
            elif bill == 10:
                ten_dollar_count += 1
                five_dollar_count -= 1
            else:
                if ten_dollar_count > 0:
                    ten_dollar_count -= 1
                    five_dollar_count -= 1
                else:
                    five_dollar_count -= 3
            if five_dollar_count < 0:
                return False
        return True