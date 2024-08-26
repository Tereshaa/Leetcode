class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF  # Mask to simulate 32-bit integer
        MAX_INT = 0x7FFFFFFF  # Maximum positive 32-bit integer

        while b != 0:
            temp = (a & b) << 1
            a = (a ^ b) & MASK
            b = temp & MASK
        
        # If a is negative, we need to return a 32-bit signed integer
        return a if a <= MAX_INT else ~(a ^ MASK)

        