class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        res = [0] * n
        s, c = 0, 0
        for i in range(n):
            res[i] += c * i - s
            if boxes[i] == '1':
                c += 1
                s += i
        s, c = 0, 0
        for i in range(n - 1, -1, -1):
            res[i] += s - c * i
            if boxes[i] == '1':
                c += 1
                s += i
        return res
