class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """Hash table.
        """
        return Counter(s) == Counter(t)
