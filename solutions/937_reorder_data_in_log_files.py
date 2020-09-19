class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        """String.

        Running time: O(nlogn) where n is the number of logs.
        """
        l_logs, d_logs = [], []
        
        for log in logs:
            parts = log.split(' ', 1)
            
            if parts[1][0] in '0123456789':
                d_logs.append(log)
            else:
                l_logs.append(parts)
                
        l_logs.sort(key=lambda l: (l[1], l[0]))
        
        return [' '.join(l) for l in l_logs] + d_logs