class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        n=len(nums)
        number=None
        count=0
        for i in range(n):
            if count==0:
                count=1
                number=nums[i]    
            elif number==nums[i]:
                count=count+1
            else:
                count=count-1
                
        elcount=0
        for i in range(n):
            if nums[i]==number:
                elcount=elcount+1
        if elcount>(n/2):
            return number
        else:
            return -1
    

        
        
