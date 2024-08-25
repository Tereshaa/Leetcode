class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[-1 for _ in range(n)]
        def rob(i):
            if i==0:
                return nums[i]
            if i<0:
                return 0
            if dp[i]!=-1:
                return dp[i]
            pick=nums[i]+rob(i-2)
            nopick=0+rob(i-1)
            dp[i]= max(pick,nopick)
            return dp[i]
        return rob(n-1)
          
        