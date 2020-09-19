class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        """String.

        Running time: O(n) where n is the length of strings.
        """
        def get_encoded(s):
            code = []
            for i in range(1, len(s)):
                code.append((ord(s[i]) - ord(s[i-1])) % 26)
            return str(code)
        
        d = collections.defaultdict(list)
        
        for s in strings:
            code = get_encoded(s)
            d[code].append(s)
            
        return d.values()
        