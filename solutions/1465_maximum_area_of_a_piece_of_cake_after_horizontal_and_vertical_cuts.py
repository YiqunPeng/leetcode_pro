class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        """Sort.

        Running time: O(nlogn) where n == max(len(horizontalCuts), len(verticalCuts)). 
        """
        mod = 10 ** 9 + 7
        horizontalCuts.sort()
        verticalCuts.sort()
        hm = horizontalCuts[0]
        for i in range(1, len(horizontalCuts)):
            hm = max(hm, horizontalCuts[i] - horizontalCuts[i-1])
        hm = max(hm, h - horizontalCuts[-1])
        vm = verticalCuts[0]
        for i in range(1, len(verticalCuts)):
            vm = max(vm, verticalCuts[i] - verticalCuts[i-1])
        vm = max(vm, w - verticalCuts[-1])
        return (vm % mod) * (hm % mod) % mod
