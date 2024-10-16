class Solution:
    def trailingZeroes(self, n: int) -> int:
        count=0
        five=5
        while n>=five:
            count+=n//five
            five *=5
        return count
        