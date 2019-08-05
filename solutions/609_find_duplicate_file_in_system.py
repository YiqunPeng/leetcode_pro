class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        """Hash Table

        Running time: O(n) where is the number of files.
        """
        from collections import defaultdict
        
        d = defaultdict(list)
        for path in paths:
            parts = path.split(' ')
            directory, files = parts[0], parts[1:]        
            for f in files:
                idx = f.index('(')
                d[f[idx+1:-1]].append(directory + '/' + f[:idx])
        
        return [v for v in d.values() if len(v) > 1]
