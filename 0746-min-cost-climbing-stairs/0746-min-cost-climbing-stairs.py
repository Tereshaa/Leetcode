class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one=cost[0]
        two=cost[1]
        if len(cost)==2:
                return min(one,two)
        for i in range(2,len(cost)):
            current=cost[i]+min(one,two)
            one=two
            two=current
        return min(one,two)
        