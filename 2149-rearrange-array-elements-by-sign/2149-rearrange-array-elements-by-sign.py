class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[0]*n
        pos=0
        neg=1
        for i in range(n):
            if nums[i]<0:
                ans[neg]=nums[i]
                neg=neg+2
            elif nums[i]>0:
                ans[pos]=nums[i]
                pos=pos+2
        return ans
        
        
        
#         brute force
        # negative=[]
        # positive=[]
        # n=len(nums)
        # final=[]*n
        # for i in range(n):
        #     if nums[i]<0:
        #         negative.append(nums[i])
        #     elif nums[i]>0:
        #         positive.append(nums[i])
        # for i in range(len(positive)):
        #     nums[2*i]=positive[i]
        # for i in range(len(negative)):
        #     nums[2*i+1]=negative[i]
        # return nums