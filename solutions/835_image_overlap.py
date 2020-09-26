class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        """Array.

        Running time: O(n^2 + AB) where is n is the length of img1, A is the number of 1s in img1 and B is the number of 1s in img2.
        """
        n = len(img1)
        pimg1 = []
        pimg2 = []
        for i in range(n):
            for j in range(n):
                if img2[i][j] == 1:
                    pimg2.append((i, j))
                if img1[i][j] == 1:
                    pimg1.append((i, j))
        d = collections.defaultdict(int)
        for i1, j1 in pimg1:
            for i2, j2 in pimg2:
                d[(i1-i2, j1-j2)] += 1
        return max(d.values() or [0])
