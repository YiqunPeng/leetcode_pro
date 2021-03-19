class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        """Hash table.
        """
        res = ''
        s = 1
        if numerator < 0:
            numerator = -numerator
            s = -s
        if denominator < 0:
            denominator = -denominator
            s = -s
        if s == -1:
            res = '-'
        d, m = divmod(numerator, denominator)
        if m == 0:
            return res + str(d) if d else '0'
        else:
            res += str(d) + '.'
        deci = []
        dic = {}
        while m != 0:
            d, m = divmod(m * 10, denominator)
            if (d, m) in dic:
                idx = dic[(d, m)]
                return res + ''.join(deci[:idx]) + '(' + ''.join(deci[idx:]) + ')'
            dic[(d, m)] = len(deci)
            deci.append(str(d))
        return res + ''.join(deci)
