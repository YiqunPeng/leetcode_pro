class Solution:
    def jump(self, nums: List[int]) -> int:
        """BFS.

        Running time: O(n) where n == len(nums).
        """
        res = 0
        m = 0
        q = deque([(0, 0)])
        while q:
            pos, step = q.popleft()
            if pos >= len(nums) - 1:
                return step
            for i in range(m+1, pos+nums[pos]+1):
                q.append((i, step+1))
            m = max(m, pos+nums[pos])
