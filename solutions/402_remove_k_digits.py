class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        """Stack.

        Running time: O(n) where n is the length of num.
        """
        if k == len(num):
            return '0'
        
        s = []
        
        for n in num:
            if not k or not s and n != '0':
                s.append(n)
                continue
            
            while s and k and s[-1] > n:
                s.pop()
                k -= 1
            
            if s or n != '0':
                s.append(n)
        
        while k:
            s.pop()
            k -= 1
                
        return ''.join(s)