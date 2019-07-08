class Solution:
    def isHappy(self, n: int) -> bool:
        def get_sum(n):
            r = 0
            while n != 0:
                m = n % 10
                r += m * m
                n //= 10
            return r
        
        s = set()
        while n not in s:
            s.add(n)
            n = get_sum(n)
            
            if n == 1:
                return True
            elif n in s:
                return False
