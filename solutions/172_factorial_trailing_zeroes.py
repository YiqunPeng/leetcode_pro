class Solution:
    def trailingZeroes(self, n: int) -> int:
        ret = 0     
        base = 5
        
        while n >= base:
            ret += n // base
            base *= 5
            
        return ret
