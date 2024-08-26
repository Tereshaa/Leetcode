class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        prev1=nums[0]
        prev2=0
        for i in range(1,n):
            take=nums[i]
            if i>1:
                take+=prev2
            notake=0+prev1
            curr=max(take,notake)
            prev2=prev1
            prev1=curr
        return prev1
        
        
        
        
        
        
        #tabulization
#         n=len(nums)
#         dp=[-1 for _ in range(n)]
#         dp[0]=nums[0]
        
#         for i in range(1,n):
#             take=nums[i]
#             if i>1:
#                 take+=dp[i-2]
#             notake=0+dp[i-1]
#             dp[i]=max(take,notake)
#         return dp[n-1]
            
