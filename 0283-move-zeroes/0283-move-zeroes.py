class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n=len(nums)
        zeroes=0
        for i in range(n):
            if nums[i]!=0:
                nums[zeroes],nums[i]=nums[i],nums[zeroes]
                zeroes=zeroes+1
        return nums
              
        
        
            
        