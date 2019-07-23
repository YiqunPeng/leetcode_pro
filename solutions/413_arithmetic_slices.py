class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        n = len(A)       
        if n < 3:
            return 0
        
        ret = 0
        c = 2
        for i in range(2, n):
            if 2 * A[i-1] == A[i - 2] + A[i]:
                c += 1
            else:
                ret += (c - 1) * (c - 2) // 2
                c = 2
        
        if c > 2:
            ret += (c - 1) * (c - 2) // 2
        return ret
