class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        """BFS.

        Running time: O(n) where n is the length of nums.
        """
        v = set()
        ret = 0
        
        for i in range(len(nums)):
            if ret >= len(nums) - i:
                break     
            if i in v:
                continue
            
            t, p = 0, i
            while p not in v:
                v.add(p)
                p = nums[p]
                t += 1
            
            ret = max(ret, t)
            
        return ret