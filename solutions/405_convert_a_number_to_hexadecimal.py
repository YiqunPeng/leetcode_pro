class Solution:
    def toHex(self, num: int) -> str:
        bits = [0] * 32
        abs_num = abs(num)
        p = 0
        while abs_num != 0:
            bits[p] = abs_num & 1
            p += 1
            abs_num >>= 1
        
        if num < 0:
            for i in range(32):
                bits[i] = 1 - bits[i]
            bits[0] += 1
            p = 0
            while p < 32 and bits[p] > 1:
                bits[p] = 0
                if p < 31:
                    bits[p+1] += 1
                p += 1
        
        res = []
        for i in range(8):
            v = bits[i*4] + bits[i*4+1] * 2 + bits[i*4+2] * 4 + bits[i*4+3] * 8
            if v < 10:
                res += [str(v)]
            else:
                res += [chr(ord('a') + v - 10)]
        while len(res) > 1 and res[-1] == '0':
            res.pop()
        return ''.join(res[::-1])