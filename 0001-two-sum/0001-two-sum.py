class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nummap={}
        for i,num in enumerate(nums):
            diff=target-nums[i]
            if diff in nummap:
                return [i,nummap[diff]]
            nummap[num]=i
            
            
