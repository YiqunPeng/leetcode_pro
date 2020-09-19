class Solution:
    def reverseVowels(self, s: str) -> str:
        """String.

        Running time: O(n) where n is the length of s.
        """
        vowels = []
        for c in s:
            if c in ('a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'):
                vowels.append(c)
                
        ls = list(s)
        for i in range(len(ls)):
            if ls[i] in ('a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'):
                ls[i] = vowels.pop()
            
        return ''.join(ls)
