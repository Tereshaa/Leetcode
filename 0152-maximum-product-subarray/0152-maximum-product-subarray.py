class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=max(nums)
        curmin=1
        curmax=1
        for num in nums:
            if num==0:
                curmin=1
                curmax=1
                continue
            temp=num*curmax
            curmax=max(num,num*curmax,num*curmin)
            curmin=min(num,temp,num*curmin)
            res=max(res,curmax)
        return res
      
            
         