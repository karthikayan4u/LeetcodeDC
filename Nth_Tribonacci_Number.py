class Solution:
    def tribonacci(self, n: int) -> int:
        a = 0
        b = 1
        c = 1
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        num = 3
        while num <= n:
            d = a + b + c
            a = b
            b = c
            c = d
            num += 1
        return d
                
        
        Time : O(n)
        Space : O(1)
