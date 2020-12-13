class Solution:
    def countAndSay(self, n: int) -> str:
        """String.

        Running time: O(nm) where m is the length of output string.
        """
        s = '1'
        c = 1
        for i in range(1, n):
            ns = ''
            c = 1
            for j in range(1, len(s)):
                if s[j] != s[j-1]:
                    ns += str(c) + s[j-1]
                    c = 1
                else:
                    c += 1
            s = ns + str(c) + s[-1]
        return s
        