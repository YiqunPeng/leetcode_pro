class Solution:
    def canTransform(self, start: str, end: str) -> bool:
    	"""String.

    	Running time: O(n) where n is the length of start.
    	"""
        if start.replace('X', '') != end.replace('X', ''):
            return False
        
        r_pos = []
        for i, c in enumerate(end):
            if c == 'R':
                r_pos.append(i)
                        
        l = len(start) - 1
        for i in range(len(start)-1, -1, -1):
            c = start[i]
            if c == 'L':
                l = i - 1
            elif c == 'R':
                if i > r_pos[-1] or i > l:
                    return False
                r_pos.pop()
                l -= 1
                
        l_pos = []
        for i, c in enumerate(end):
            if c == 'L':
                l_pos.append(i)
                
        l_pos = l_pos[::-1]
                
        r = 0
        for i, c in enumerate(start):
            if c == 'R':
                r = i + 1
            elif c == 'L':
                if i < r or i < l_pos[-1]:
                    return False
                l_pos.pop()
                r += 1
        
        return True  
        