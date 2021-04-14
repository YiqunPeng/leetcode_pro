class Solution:
    def confusingNumber(self, N: int) -> bool:
        rotate = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        new = []
        for c in str(N):
            if c not in rotate:
                return False
            new.append(rotate[c])
        return N != int(''.join(new[::-1]))
