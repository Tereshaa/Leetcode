class Solution:
    def findMin(self, nums: List[int]) -> int:
        low=0
        high=len(nums)-1
        res=nums[0]
        
        while low<=high:
            mid=(low+high)//2
            if nums[low]<nums[high]:
                res=min(nums[low],res)
                break
            res=min(nums[mid],res)
            if nums[mid]>=nums[low]:           
                low=mid+1
            else:
                high=mid-1
        return res
                          
                
                