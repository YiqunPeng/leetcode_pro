from collections import deque

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
    	"""Queue.

    	Running time: O(n) where n is the length of deck.
    	"""
        n = len(deck)
        pos = deque(range(n))
        res = [0] * n
        for v in sorted(deck):
            res[pos.popleft()] = v
            if pos:
                pos.append(pos.popleft())
        return res
