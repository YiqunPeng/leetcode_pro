class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        """Hash set.

        Running time: O(n) where n is the length arr.
        """
        a = set()
        z = 0
        for i in arr:
            if i == 0:
                z += 1
            a.add(i)
        
        if z > 1:
            return True
        
        for i in arr:
            if i and 2 * i in arr:
                return True
        return False
        