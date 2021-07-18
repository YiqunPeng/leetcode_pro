class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """String.

        Running time: O(n) where n == len(s).
        """
        left, right = 0, 0
        for c in s:
            if c == ')':
                right += 1
        res = []
        for c in s:
            if c == '(':
                if right == left:
                    continue
                left += 1
            elif c == ')':
                right -= 1
                if left == 0:
                    continue
                left -= 1
            res.append(c)
        return ''.join(res)
