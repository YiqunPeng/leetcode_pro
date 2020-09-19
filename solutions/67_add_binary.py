class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """String.

        Running time: O(n) where n is the max length between a and b.
        """
        a, b = list(a), list(b)
        
        if len(a) < len(b):
            a, b = b, a
        
        p_a, p_b = len(a) - 1, len(b) - 1
        c = 0
        
        while p_b >= 0:
            if a[p_a] == '0' and b[p_b] == '0':
                a[p_a] = str(c)
                c = 0
            
            elif (a[p_a] == '0' and b[p_b] == '1') or (a[p_a] == '1' and b[p_b] == '0'):
                if c == 0:
                    a[p_a] = '1'
                else:
                    a[p_a] = '0'
            
            else:
                if c == 0:
                    a[p_a] = '0'
                    c = 1
                else:
                    a[p_a] = '1'
                    
            p_a -= 1
            p_b -= 1
            
        while p_a >= 0:
            if c == 1:
                if a[p_a] == '1':
                    a[p_a] = '0'
                else:
                    a[p_a] = '1'
                    c = 0
            p_a -= 1
            
        if c == 1:
            a = ['1'] + a
            
        return ''.join(a)
                
        