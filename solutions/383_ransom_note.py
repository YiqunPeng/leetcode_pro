class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    	"""Hash Table.
		
		Running time: O(r + m) where r is the length of ransomNote and m is the length of magazine.
    	"""
        rc = collections.Counter(ransomNote)
        mc = collections.Counter(magazine)
        
        for k, v in rc.items():
            if k not in mc or v > mc[k]:
                return False
        return True
        