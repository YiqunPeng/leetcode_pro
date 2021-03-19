class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        res = []
        q = deque(list(range(1, 10)))
        while q:
            num = q.popleft()
            if len(str(num)) == n:
                res.append(num)
                continue
            d = num % 10
            if 0 <= d + k < 10:
                q.append(num * 10 + d + k)
            if 0 <= d - k < 10 and k != 0:
                q.append(num * 10 + d - k)
        return res
