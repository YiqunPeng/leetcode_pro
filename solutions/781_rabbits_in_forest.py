class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        """Math.

        Running time: O(n) where n is the length of answers.
        """
        c = collections.Counter(answers)
        
        ret = 0
        
        for k, v in c.items():
            if k == 0:
                ret += v
                continue
                
            if v % (k + 1) == 0:
                ret += v
            else:
                ret += (v // (k + 1) + 1) * (k + 1)
        
        return ret