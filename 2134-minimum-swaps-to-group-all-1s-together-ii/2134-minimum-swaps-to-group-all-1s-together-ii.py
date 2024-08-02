class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        total_ones = nums.count(1)
        l = 0
        ones = 0
        max_ones = 0
        
        for r in range(2 * n):
            if nums[r % n] == 1:
                ones += 1
            if r - l + 1 > total_ones:
                ones -= nums[l % n]
                l += 1       
            max_ones = max(ones, max_ones)
        return total_ones - max_ones