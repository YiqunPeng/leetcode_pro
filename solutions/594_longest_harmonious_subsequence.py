class Solution:
    def findLHS(self, nums: List[int]) -> int:
        """Hash table.

        Running time: O(nlogn) where n is the length of nums.
        """
        d = collections.defaultdict(int)
        for num in nums:
            d[num] += 1
            
        keys = sorted(d.keys())
        ret = 0
        
        for i in range(1, len(keys)):
            if keys[i] - keys[i-1] == 1:
                ret = max(ret, d[keys[i]] + d[keys[i-1]])
        
        return ret