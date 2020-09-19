class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        """String.

        Running time: O(a + b) where a is the length of A and b is the length of B.
        """
        a_words = A.split(' ')
        b_words = B.split(' ')
        
        a_dict = Counter(a_words)
        b_dict = Counter(b_words)
        
        res = []
        
        for k, v in a_dict.items():
            if v == 1 and k not in b_dict:
                res.append(k)
        for k, v in b_dict.items():
            if v == 1 and k not in a_dict:
                res.append(k)
        
        return res
