class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if N == 0: return 1
        
        ans = 0
        i = 0
        
        while N:
            r = N % 2 
            ans += 2 ** i * (1 - r)
            i += 1
            N //= 2
            
        return ans
