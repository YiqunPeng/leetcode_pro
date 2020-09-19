class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    	"""Sort.

    	Running time: O(nmlogm) where n is the length of strs and m is the length of each string.
    	"""
        d = collections.defaultdict(list)
        
        for s in strs:
            d[str(sorted(s))].append(s)
        
        return d.values()