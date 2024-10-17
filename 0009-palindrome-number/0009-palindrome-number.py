class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        original=x
        reversed=0
        while x:
            digit=x%10
            reversed=reversed*10+digit
            x=x//10
        return original==reversed
        # x=str(x)
        # l=0
        # r=len(x)-1
        # while l<=r:
        #     if x[l]!=x[r]:
        #         return False
        #     l+=1
        #     r-=1
        # return True
        