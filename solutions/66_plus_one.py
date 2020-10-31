class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """Array.

        Running time: O(n) where n is the length of digits.
        """
        c = 1
        for i in range(len(digits) - 1, -1, -1):
            c, digits[i] = divmod(digits[i] + c, 10)
        return digits if not c else [1] + digits
