class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """String.

        Running time: O(n) where n == len(s).
        """
        l = list(s)
        p = []
        for i in range(len(s)):
            if s[i] == '(':
                p.append(i)
            elif s[i] == ')':
                if not p:
                    l[i] = ''
                else:
                    p.pop()
        while p:
            l[p.pop()] = ''
        return ''.join(l)
