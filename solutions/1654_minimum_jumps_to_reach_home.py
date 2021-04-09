class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        if x == 0:
            return 0
        forb = set(forbidden)
        if a in forb:
            return -1
        q = deque([(a, 'f', 1)])
        v = set([(a, 'f')])
        while q:
            pos, dr, j = q.popleft()
            if pos == x:
                return j
            if pos + a not in forb and (pos + a, 'f') not in v and pos + a <= 6000:
                v.add((pos+a, 'f'))
                q.append((pos+a, 'f', j+1))
            if dr == 'f' and pos - b >= 0 and pos - b not in forb and (pos-b, 'b') not in v:
                v.add((pos-b, 'b'))
                q.append((pos-b, 'b', j+1))
        return -1
