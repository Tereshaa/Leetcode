class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        sumtotal=(n*(n+1))/2
        sumquestion=0
        for i in range(n):
            sumquestion=sumquestion + nums[i]
        return int(sumtotal-sumquestion)
            
        