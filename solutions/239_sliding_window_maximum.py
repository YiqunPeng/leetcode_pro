class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """Deque.

        Running time: O(n) where n == len(nums).
        """
        q = deque()
        res = []
        for i in range(k):
            while q and q[-1] < nums[i]:
                q.pop()
            q.append(nums[i])
        res.append(q[0])
        for i in range(k, len(nums)):
            while q and q[-1] < nums[i]:
                q.pop()
            q.append(nums[i])
            if nums[i-k] == q[0]:
                q.popleft()
            res.append(q[0])
        return res
