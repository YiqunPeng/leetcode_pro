class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
    	"""Hash table

    	Running Time: O(c) where c is total amount of char in words.
    	"""
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        return len(set(''.join(morse[ord(c) - ord('a')] for c in word) for word in words))
