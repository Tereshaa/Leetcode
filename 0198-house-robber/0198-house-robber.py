class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        prev2=0
        prev1=nums[0]
        for i in range(1,n):
            if i>0:
                pick=nums[i] +prev2
            nopick=0+prev1
            cur=max(pick,nopick)
            prev2=prev1
            prev1=cur
        return prev1

            
#         def rob(i):
#             if i==0:
#                 return nums[i]
#             if i<0:
#                 return 0
#             if dp[i]!=-1:
#                 return dp[i]
#             pick=nums[i]+rob(i-2)
#             nopick=0+rob(i-1)
#             dp[i]= max(pick,nopick)
#             return dp[i]
#         return rob(n-1)
    
