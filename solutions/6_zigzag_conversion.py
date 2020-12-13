class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """Array

        Running Time: O(n) where n is the length of s.
        """
        if numRows == 1:
            return s
        arr = ['' for i in range(numRows)]
        r = 0
        d = True
        for i in s:
            arr[r] += i
            if d:
                if r == numRows - 1:
                    r -= 1
                    d = False
                else:
                    r += 1
            else:
                if r == 0:
                    r += 1
                    d = True
                else:
                    r -= 1
        return ''.join(arr)
 