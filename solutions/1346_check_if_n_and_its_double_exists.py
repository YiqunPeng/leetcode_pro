class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
    	"""Hash set.

    	Running time: O(n) where n == len(arr).
    	"""
        s = set()
        for a in arr:
            if a * 2 in s or (a % 2 == 0 and a // 2 in s):
                return True
            s.add(a)
        return False
