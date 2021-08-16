class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        """Backtracking.
        """
        if len(cards) == 1 and abs(cards[0] - 24.0) < 0.0001:
            return True
        for i in range(1, len(cards)):
            for j in range(0, i):
                copy = cards[:]
                a, b = copy[i], copy[j]
                copy.pop(i)
                copy.pop(j)
                nxt = [a + b, a - b, b - a, a * b]
                if a != 0.0:
                    nxt.append(b / a)
                if b != 0.0:
                    nxt.append(a / b)
                for n in nxt:
                    if self.judgePoint24(copy + [n]):
                        return True
        return False
