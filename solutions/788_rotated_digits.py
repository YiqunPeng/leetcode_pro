class Solution:
    def rotatedDigits(self, N: int) -> int:
        """String.
        """
        res = 0
        for i in range(1, N + 1):
            v = str(i)
            for j in ['3', '4', '7']:
                if j in v:
                    break
            else:
                for j in ['2', '5', '6', '9']:
                    if j in v:
                        res += 1
                        break
        return res
