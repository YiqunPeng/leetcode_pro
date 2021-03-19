class Solution:
    def pathSum(self, nums: List[int]) -> int:
        res = 0
        cnt = defaultdict(int)
        for num in nums[::-1]:
            num = str(num)   
            d, p, v = int(num[0]), int(num[1]), int(num[2])
            res += v * cnt.get((d, p), 1)
            cnt[(d-1, (p+1)//2)] += cnt.get((d, p), 1)
        return res
