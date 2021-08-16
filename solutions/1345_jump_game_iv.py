class Solution:
    def minJumps(self, arr: List[int]) -> int:
        """BFS.
        """
        n = len(arr)
        vals = defaultdict(list)
        for i in range(n):
            vals[arr[i]].append(i)
        q = deque([(0, 0)])
        visited = set([0])
        while q:
            idx, jump = q.popleft()
            if idx == n - 1:
                return jump
            if idx - 1 >= 0 and idx - 1 not in visited:
                q.append((idx - 1, jump + 1))
                visited.add(idx - 1)
            if idx + 1 < n and idx + 1 not in visited:
                q.append((idx + 1, jump + 1))
                visited.add(idx + 1)
            for i in vals[arr[idx]]:
                if i not in visited:
                    q.append((i, jump + 1))
                    visited.add(i)
            vals[arr[idx]] = []
