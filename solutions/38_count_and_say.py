class Solution:
    def countAndSay(self, n: int) -> str:
        """String.

        Running time: O(nm) where m is the length of output string.
        """
        num = '1'
        res = '1'
        
        for i in range(1, n):
            res = ''
            c = 1
            p = 1
            while p < len(num):
                if num[p] == num[p-1]:
                    c += 1
                else:
                    res = res + str(c) + str(num[p-1])
                    c = 1
                p += 1
            res = res + str(c) + num[-1]
            num = res
            
        return res
        