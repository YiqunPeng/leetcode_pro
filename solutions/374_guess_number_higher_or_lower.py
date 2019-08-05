# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """Binary search.

        Running time: O(nlogn)
        """
        l, r = 0, n
        while l <= r:
            m = l + (r - l) // 2
            res = guess(m)
            if res == 0:
                return m
            elif res == -1:
                r = m - 1
            else:
                l = m + 1
