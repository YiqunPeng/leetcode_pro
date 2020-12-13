class Solution:
    def checkValidString(self, s: str) -> bool:
        """String.

        Running time: O(n) where n == len(s).
        """
        cmin = cmax = 0
        for i in s:
            if i == '(':
                cmin += 1
                cmax += 1
            elif i == '*':
                cmax += 1
                cmin = max(cmin - 1, 0)
            else:
                cmax -= 1
                cmin = max(cmin - 1, 0)
            if cmax < 0:
                return False
        return cmin == 0
