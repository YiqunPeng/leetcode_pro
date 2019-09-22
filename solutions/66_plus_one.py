class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """Array.

        Running time: O(n) where n is the length of digits.
        """
        digits[-1] += 1
        
        p = len(digits) - 1
        while p and digits[p] > 9:
            digits[p] -= 10
            digits[p-1] += 1
            p -= 1
        
        if digits[0] > 9:
            digits[0] -= 10
            digits = [1] + digits
        
        return digits