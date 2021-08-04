class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        p = 0
        while p < len(data):
            b = self._get_binary(data[p])
            one = 0
            for c in b:
                if c == '1':
                    one += 1
                else:
                    break
            if one == 0:
                p += 1
                continue
            if p + one - 1 >= len(data) or one > 4 or one == 1:
                return False
            if not self._validate(data[p+1:p+one]):
                return False
            p += one
        return True
    
    def _validate(self, seq):
        for s in seq:
            b = self._get_binary(s)
            if b[:2] != '10':
                return False
        return True
    
    def _get_binary(self, num):
        b = bin(num)[2:]
        return '0' * (8 - len(b)) + b
