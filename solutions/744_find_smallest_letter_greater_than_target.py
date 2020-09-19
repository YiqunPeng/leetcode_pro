class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        """Binary Search.

        Running time: O(nlogn) where n is the length of letters.
        """
        if target >= letters[-1] or target < letters[0]:
            return letters[0]
        
        l, r = 0, len(letters)
        while l < r:
            m = l + (r - l) // 2
            if letters[m - 1] <= target < letters[m]:
                return letters[m]
            elif target < letters[m - 1]:
                r = m
            else:
                l = m
                