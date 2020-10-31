class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        """String.

        Running time: O(nlogn) where n == len(s1).
        """
        s1 = sorted(s1)
        s2 = sorted(s2)
        s1bs2, s2bs1 = True, True
        for i in range(len(s1)):
            if s1[i] < s2[i]:
                s1bs2 = False
            if s2[i] < s1[i]:
                s2bs1 = False
        return s1bs2 or s2bs1
