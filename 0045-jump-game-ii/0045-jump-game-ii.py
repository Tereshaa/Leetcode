class Solution:
    def jump(self, nums: List[int]) -> int:
        res=0
        l=0
        r=0
        
        while r<len(nums)-1:
            maxi=0
            for i in range(l,r+1):
                maxi=max(maxi,i+nums[i])
            l=r+1
            r=maxi
            res+=1
        return res
            
            
        