class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 2 or n == 1:
            return 1
        n_o = 0
        n_i = 1
        n_ii = 1
        for i in range(2,n):
            tmp = n_o + n_i + n_ii
            n_o = n_i
            n_i = n_ii
            n_ii = tmp
        return tmp
