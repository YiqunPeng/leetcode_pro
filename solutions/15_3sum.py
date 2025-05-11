class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """

        Running time: O(n^2) where n == len(nums).
        """
        ctr = Counter(nums)
        keys = sorted(ctr.keys())
        res = []
        for i in range(len(keys)):
            if keys[i] > 0:
                break
            for j in range(i, len(keys)):
                c = -keys[i] - keys[j]
                if c < keys[j] or c not in ctr:
                    continue
                if keys[i] == keys[j] == c and ctr[c] < 3:
                    continue
                if keys[i] == keys[j] and ctr[keys[i]] < 2:
                    continue
                if keys[j] == c and ctr[c] < 2:
                    continue
                res.append([keys[i], keys[j], c])
        return res
