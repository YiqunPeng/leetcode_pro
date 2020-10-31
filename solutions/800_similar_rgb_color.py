class Solution:
    def similarRGB(self, color: str) -> str:
    	"""Hash Table

    	Running Time: O(1)
    	"""
        d = [i * 16 + i for i in range(16)]
        hexa = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f':15}
        deci = {0: '00', 1: '11', 2: '22', 3: '33', 4: '44', 5: '55', 6: '66', 7: '77', 8: '88',
                9: '99', 10: 'aa', 11: 'bb', 12: 'cc', 13: 'dd', 14: 'ee', 15: 'ff'}
        res = '#'
        for i in range(1, 6, 2):
            v = 16 * hexa[color[i]] + hexa[color[i+1]]
            idx = bisect.bisect_left(d, v)
            if idx == 0 or d[idx] - v <= v - d[idx-1]:
                res = res + deci[idx]
            else:
                res = res + deci[idx-1]
        return res
           