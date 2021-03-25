class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        pos, neg = 0, -1
        res = [0]
        for c in S:
            if c == 'I':
                pos += 1
                res.append(pos)
            else: 
                res.append(neg)
                neg -= 1
        neg += 1
        for i in range(len(res)):
            res[i] -= neg
        return res
