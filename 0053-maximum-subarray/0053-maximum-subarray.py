import sys
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        maxi= - sys.maxsize
        sum=0
        for i in range(n):
            sum=sum+nums[i]
            if sum>maxi:
                maxi=sum
            if sum<0:
                sum=0
        return maxi
    
    
#     to find subarray
#         n=len(nums)
#         start=0
#         ansstart=-1
#         ansend=-1
    
#         maxi = -sys.maxsize - 1
#         sum=0
#         for i in range(n):
#             if sum==0:
#                 start=i
#             sum=sum+nums[i]
#             if(sum>maxi):
#                 maxi=sum
#                 ansstart=start
#                 ansend=i
#             if(sum<0):
#                 sum=0
#         for i in range(ansstart,ansend+1):
#             print(nums[i])
         
        