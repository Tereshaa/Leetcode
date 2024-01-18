import sys
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        maxi = -sys.maxsize - 1
        sum=0
        for i in range(n):
            sum=sum+nums[i]
            if(sum>maxi):
                maxi=sum
            if(sum<0):
                sum=0
        return maxi
            
        