class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        """Math.

        Running time: O(n) where n is the length of answers.
        """
        d = {}
        res = 0
        for a in answers:
            if a not in d or d[a] == 0:
                res += a + 1
                d[a] = a
            else:
                d[a] -= 1
        return res
