class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        q = deque([('0000', 0)])
        seen = set(['0000'])
        while q:
            lock, step = q.popleft()
            if lock in deadends:
                continue
            if lock == target:
                return step
            for i in range(4):
                a = lock[:i] + str((int(lock[i]) + 1) % 10) + lock[i+1:]
                b = lock[:i] + str((int(lock[i]) - 1) % 10) + lock[i+1:]
                if a not in seen:
                    seen.add(a)
                    q.append((a, step + 1))
                if b not in seen:
                    seen.add(b)
                    q.append((b, step + 1))
        return -1
        