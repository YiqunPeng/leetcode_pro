class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        """Array

        Running time: O(n) where n is the length of bits.
        """
        n = len(bits)
        
        if n == 1:
            return True
        if n == 2:
            return bits[0] == 0
        
        k = 0
        while k < n:
            if (k == n - 2 and bits[k] == 0) or k == n - 1:
                return True
            
            if bits[k] == 0:
                k += 1
            else:
                k += 2
                
        return False