class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        q = deque([('', n, n, 0)])
        while q:
            temp, l, r, unmatched = q.popleft()
            if l == r == 0:
                res.append(temp)
                continue
            if l > 0:
                q.append((temp + '(', l-1, r, unmatched+1))
            if r > 0 and unmatched > 0:
                q.append((temp + ')', l, r-1, unmatched-1))
        return res
