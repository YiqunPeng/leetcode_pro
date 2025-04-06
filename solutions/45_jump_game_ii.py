class Solution:
    def jump(self, nums: List[int]) -> int:
        """BFS.

        Running time: O(n) where n == len(nums).
        """
        q = collections.deque([(0, 0)])
        r = 0
        while q:
            idx, s = q.popleft()
            if idx >= len(nums) - 1:
                return s
            for ni in range(r + 1, idx + nums[idx] + 1):
                q.append((ni, s + 1))
            r = max(r, idx + nums[idx])
