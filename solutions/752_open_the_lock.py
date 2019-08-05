class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        """BFS.

        Running time: O(n) where n is the number of all possible states.
        """
        def helper(c, q, v, d, m):
            if c not in d and c not in v:
                v.add(c)
                q.append((c, m + 1))
        
        from collections import deque
        
        if target == '0000':
            return 0
        
        deadends = set(deadends)
        if '0000' in deadends:
            return -1
        
        v = set(['0000'])   
        q = deque([('0000', 0)])
        while q:
            code, m = q.popleft()
            
            for i in range(4):
                n = int(code[i])
                up = code[:i] + str((n - 1) % 10) + code[i+1:]
                down = code[:i] + str((n + 1) % 10) + code[i+1:]
                if up == target or down == target:
                    return m + 1
                helper(up, q, v, deadends, m)
                helper(down, q, v, deadends, m)

        return -1
        