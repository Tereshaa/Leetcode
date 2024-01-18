class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        numindices=[(nums[i],i)for i in range(n)]
        numindices.sort()
        left=0
        right=n-1  
        while(left<right):
            sum=numindices[left][0]+numindices[right][0]
            if sum<target:
                left=left+1
            elif sum>target:
                right=right-1
            elif sum==target:
                return [numindices[left][1],numindices[right][1]]
            
            
            
            #brute force
#         for i in range(n-1):
#             for j in range(1,n):
#                 if nums[i]+nums[j]==target and i!=j:
#                     return [i,j]

#hashmap


        