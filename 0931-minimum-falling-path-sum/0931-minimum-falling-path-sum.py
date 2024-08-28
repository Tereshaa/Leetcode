class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows=len(matrix)
        cols=len(matrix[0])
        dp=[[0 for _ in range(cols)] for _ in range(rows)]
        dp[-1] = matrix[-1][:]
        for i in range(rows-2,-1,-1):
            for j in range(cols):
                up=matrix[i][j]+dp[i+1][j]
                ldiag=matrix[i][j]+dp[i+1][j-1] if j>0 else float("inf")
                rdiag=matrix[i][j]+dp[i+1][j+1] if j<cols-1 else float("inf")
                dp[i][j]=min(up,ldiag,rdiag)
        return min(dp[0])
  