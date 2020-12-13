class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        words = [i for i in words if i]
        return ' '.join(words[::-1])
