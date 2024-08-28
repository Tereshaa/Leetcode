class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)  # Initialize the result with the maximum value in nums
        curmin = 1  # Initialize current minimum product to 1
        curmax = 1  # Initialize current maximum product to 1
        
        for num in nums:
            if num == 0:  # If the current number is 0
                curmin = 1  # Reset curmin to 1
                curmax = 1  # Reset curmax to 1
                continue  # Skip the rest of the loop and move to the next iteration
            
            # Since curmin will be updated in curmax's calculation, store curmax temporarily
            temp_max = num * curmax
            
            # Update curmax and curmin
            curmax = max(num, num * curmax, num * curmin)
            curmin = min(num, temp_max, num * curmin)
            
            # Update the result with the maximum value found so far
            res = max(res, curmax)
        
        return res  # Return the fin
        