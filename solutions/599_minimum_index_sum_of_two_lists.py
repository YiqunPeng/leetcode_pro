class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
    	"""Hash table.
    	"""
        d = {}
        for i in range(len(list1)):
            d[list1[i]] = i
        s = collections.defaultdict(list)
        for i in range(len(list2)):
            if list2[i] in d:
                s[i+d[list2[i]]].append(list2[i])
        return s[min(s.keys())]
