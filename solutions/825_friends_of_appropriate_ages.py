class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        """Hash table.
        """
        c = collections.Counter(ages)
        res = 0
        for ka, va in c.items():
            for kb, vb in c.items():
                if kb > 0.5 * ka + 7 and kb <= ka:
                    if ka == kb:
                        res += va * (va - 1)
                    else:
                        res += va * vb 
        return res
