class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        """Hash table.
        """
        c = Counter(nums)
        res = []
        m, d = None, None
        for i in range(1, len(nums) + 1):
            if i not in c:
                m = i
            if i in c and c[i] == 2:
                d = i
        return [d, m]
