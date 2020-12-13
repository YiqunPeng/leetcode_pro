class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        """Hash table.

        Running time: O(n) where n == len(croakOfFrogs).
        """
        res = 0
        d = {'c': 0, 'r': 0, 'o': 0, 'a': 0, 'k': 0}
        croak = {'c': 'k', 'r': 'c', 'o': 'r', 'a': 'o', 'k': 'a'}
        for i in croakOfFrogs:
            p = croak[i]
            if d[p] == 0:
                if p == 'k':
                    res += 1
                else:
                    return -1
            else:
                d[p] -= 1
            d[i] += 1
        if all(d[k] == 0 for k in d if k != 'k'):
            return res
        else:
            return -1
