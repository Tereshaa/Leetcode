class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        rows=len(triangle)
        dp=triangle[-1]
        for i in range(rows-2,-1,-1):
            for j in range(i+1):
                up=triangle[i][j]+dp[j]
                diagonal=triangle[i][j]+dp[j+1]
                dp[j]=min(up,diagonal)
        return dp[0]