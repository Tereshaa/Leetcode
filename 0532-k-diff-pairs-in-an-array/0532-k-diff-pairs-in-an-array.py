class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k<0:
            return 0
        unique=set()
        seen=set()
        n=len(nums)
        for num in nums:
            if num-k in seen:
                unique.add((num-k,num))
            if num+k in seen:
                unique.add((num,num+k))
            seen.add(num)
        return len(unique)