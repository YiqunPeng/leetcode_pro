class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        overlap_area = self._get_overlap(A, B, C, D, E, F, G, H)
        area_1 = self._get_area(A, B, C, D)
        area_2 = self._get_area(E, F, G, H)
        return area_1 + area_2 - overlap_area
    
    def _get_area(self, a, b, c, d):
        return (d - b) * (c - a)
    
    def _get_overlap(self, a, b, c, d, e, f, g, h):
        if a < g and e < c and b < h and f < d:
            l = min(c, g) - max(a, e)
            w = min(d, h) - max(b, f)
            return l * w
        else:
            return 0
