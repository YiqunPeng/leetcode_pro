class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
    	"""Hash table.
    	"""
        s = {'0': '0', '1': '1', '6': '9', '9': '6', '8': '8'}
        for i in range(len(num) // 2 + 1):
            if num[i] not in s or s[num[i]] != num[len(num)-1-i]:
                return False
        return True
