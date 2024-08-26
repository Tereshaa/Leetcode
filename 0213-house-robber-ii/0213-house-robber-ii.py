class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n=len(nums)
        if n==0:
            return 0
        if n==1:
            return nums[0]
        
        def rob(nums):
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
        return max(rob(nums[1:]),rob(nums[:-1]))

