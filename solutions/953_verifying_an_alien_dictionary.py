class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        """Hash table.
        """
        d = {order[i]: i for i in range(len(order))}
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            p1, p2 = 0, 0
            while p1 < len(w1) or p2 < len(w2):
                if p1 < len(w1) and p2 < len(w2):
                    if d[w1[p1]] > d[w2[p2]]:
                        return False
                    elif d[w1[p1]] < d[w2[p2]]:
                        break
                elif p1 < len(w1):
                    return False
                p1 += 1
                p2 += 1
        return True
