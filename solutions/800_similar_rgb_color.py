class Solution:
    def similarRGB(self, color: str) -> str:
    	"""Hash Table

    	Running Time: O(1)
    	"""
        def get_similar(s):
            return min(['00', '11', '22', '33', '44', '55', '66', '77', 
                        '88', '99', 'aa', 'bb', 'cc', 'dd', 'ee', 'ff'], key=lambda x: abs(int(s, 16) - int(x, 16)))
        
        ret = '#'
        for i in range(1, len(color), 2):
            ret += get_similar(color[i:i+2])
        return ret
           