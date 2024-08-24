class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target) 
        total_sum=0
        step=0
        while total_sum<target or (total_sum-target)%2!=0:
            step+=1
            total_sum+=step
        return step
