class Solution:
    def defangIPaddr(self, address: str) -> str:
    	"""String.

    	Running time: O(n) where n is the length of address.
    	"""
        return address.replace('.', '[.]')
