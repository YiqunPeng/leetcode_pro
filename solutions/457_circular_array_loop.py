class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        """DFS.
        """
        n = len(nums)
        for i in range(n):
            s = i
            t = set()
            while i not in t:
                t.add(i)
                i = (i + nums[i]) % n
                if i < 0:
                    i += n
                if nums[s] * nums[i] < 0:
                    break
            if i == s and len(t) > 1:
                return True
        return False
