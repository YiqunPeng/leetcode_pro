class Solution:

    def __init__(self, nums: List[int]):
    	"""Hash table.
		
		Running time: O(n) where n is the length of nums.
    	"""
        self.index = collections.defaultdict(list)
        for i, num in enumerate(nums):
            self.index[num].append(i)
        
    def pick(self, target: int) -> int:
    	"""Running time: O(1).
    	"""
        return random.choice(self.index[target])
