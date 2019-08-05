class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        """BFS
        
        Running time: O(nm^2) where n is the number of strings in bank and
                      m is the length of each string.
        """
        from collections import deque

        bank = set(bank)
        q = deque([(start, 0)])
        while q:
            s, m = q.popleft()
            
            for i in range(len(s)):
                for c in 'ACGT':
                    if s[i] == c:
                        continue
                    
                    ns = s[:i] + c + s[i+1:]
                    if ns in bank:
                        if ns == end:
                            return m + 1
                        bank.remove(ns)
                        q.append((ns, m + 1))

        return -1