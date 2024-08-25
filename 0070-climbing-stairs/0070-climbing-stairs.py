class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=1:
            return 1
        last=1
        seclast=1
        for i in range(2,n+1):
            current=last+seclast
            last=seclast
            seclast=current
        return current
