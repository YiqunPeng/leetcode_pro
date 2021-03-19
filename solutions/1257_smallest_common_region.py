class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        d = {}
        for region in regions:
            for i in range(1, len(region)):
                d[region[i]] = region[0]
        r1 = set([region1])
        while region1 in d:
            r1.add(d[region1])
            region1 = d[region1]
        while region2 not in r1:
            region2 = d[region2]
        return region2
