class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num=set(nums)
        longest=0

        for n in nums:
            if(n-1) not in num:
                count=1
                while (n+count) in num:
                    
                    count=count+1
                longest=max(count,longest)
        return longest
                
        