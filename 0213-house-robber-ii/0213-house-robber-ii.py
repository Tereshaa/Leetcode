class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        
        def rob(nums):
            prev2=0
            prev1=0
            for num in nums:
                pick=num+prev2
                nopick=prev1
                cur=max(pick,nopick)
                prev2=prev1
                prev1=cur
            return prev1
        rob1=rob(nums[1:])
        rob2=rob(nums[:-1])
        return max(rob1,rob2)

       