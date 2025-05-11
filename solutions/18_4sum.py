class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ctr = Counter(nums)
        res = []
        for a in range(len(nums)-3):
            if a > 0 and nums[a] == nums[a-1]:
                continue
            for b in range(a+1, len(nums)-2):
                if b > a + 1 and nums[b] == nums[b-1]:
                    continue
                for c in range(b+1, len(nums)-1):
                    if c > b + 1 and nums[c] == nums[c-1]:
                        continue
                    v = target - nums[a] - nums[b] - nums[c]
                    if v < nums[c]:
                        break
                    cnt = 1
                    for i in [a, b, c]:
                        if nums[i] == v:
                            cnt += 1
                    if cnt <= ctr[v]:
                        res.append([nums[a], nums[b], nums[c], v])
        return res