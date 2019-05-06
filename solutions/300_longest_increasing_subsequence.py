class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """DP

        Running Time: O(n^2) where n is the length of nums.
        """
        n = len(nums)
        if n == 0:
            return 0
        
        dp = [1] * n
        
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


    def lengthOfLIS_2(self, nums: List[int]) -> int:
        """Binary search

        Running Time: O(n log n) where n is the length of nums.
        """
        def binary_search(a, num):
            l, r = 0, len(a) - 1
            while l <= r:
                m = l + (r - l) // 2
                if a[m-1] < num < a[m]:
                    a[m] = num
                    return 
                elif a[m] > num:
                    r = m - 1
                else:
                    l = m + 1
        
        n = len(nums)
        if n == 0:
            return 0
        
        a = [nums[0]]
        
        for num in nums[1:]:
            if num < a[0]:
                a[0] = num
            elif num > a[-1]:
                a.append(num)
            else:
                binary_search(a, num)

        return len(a)
