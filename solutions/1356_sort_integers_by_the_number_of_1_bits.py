class Solution:
    
    def __init__(self):
        self.memo_1_bits = {}
    
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda x: (self._count_1_bits(x), x))
        
    def _count_1_bits(self, a):
        if a in self.memo_1_bits:
            return self.memo_1_bits[a]
        c = bin(a).count('1')
        self.memo_1_bits[a] = c
        return c
