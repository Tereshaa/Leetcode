class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        for i in range(n-1):
            for j in range(1,n):
                if nums[i]+nums[j]==target and i!=j:
                    return [i,j]
        