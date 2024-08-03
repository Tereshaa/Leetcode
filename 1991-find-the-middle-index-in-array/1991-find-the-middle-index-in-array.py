class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        totsum=0
        for i in range(0,len(nums)):
            totsum+=nums[i]
        leftsum=0
        for i in range(0,len(nums)):
            rightsum=totsum-leftsum-nums[i]
            if rightsum==leftsum:
                return i
            leftsum+=nums[i]
        return -1