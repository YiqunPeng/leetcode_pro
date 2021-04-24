class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        gdis = float('inf')
        for a, b in ghosts:
            gdis = min(gdis, abs(target[0] - a) + abs(target[1] - b))
        return gdis > abs(target[0]) + abs(target[1])
