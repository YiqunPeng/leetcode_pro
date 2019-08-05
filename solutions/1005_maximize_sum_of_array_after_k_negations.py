class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        a_sum = sum(A)
        
        pos, neg = [], []
        min_abs_v = abs(A[0])
        for a in A:
            if a > 0:
                pos.append(a)
            elif a < 0:
                neg.append(a)
            min_abs_v = min(min_abs_v, abs(a))
        
        if K <= len(neg):
            return a_sum - 2 * sum(sorted(neg)[:K])
        else:
            a_sum = a_sum - 2 * sum(neg)
            if (K - len(neg)) % 2 == 1:
                a_sum -= 2 * min_abs_v
            return a_sum
