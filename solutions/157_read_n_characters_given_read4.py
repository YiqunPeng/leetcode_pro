class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        res = 0     
        while n > 0:
            buf4 = [' '] * 4
            m = read4(buf4)
            buf[res:res+4] = buf4
            if m == 0:
                return res
            if n <= m <= 4:
                return res + n
            n -= m
            res += m
        return res
