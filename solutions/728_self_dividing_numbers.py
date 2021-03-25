class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for i in range(left, right + 1):
            if self._self_dividing(i):
                res.append(i)
        return res
    
    def _self_dividing(self, n):
        for c in str(n):
            if c == '0' or n % int(c) != 0:
                return False
        return True
