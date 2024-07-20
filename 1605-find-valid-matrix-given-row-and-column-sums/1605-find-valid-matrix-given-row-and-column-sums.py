class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        rows=len(rowSum)
        cols=len(colSum)
        
        matrix=[[0]*cols for _ in range(rows)]
        
        for r in range(rows):
            matrix[r][0]=rowSum[r]
            
        for c in range(cols):
            currentcolsum=0
            for r in range(rows):
                currentcolsum += matrix[r][c]
            
            r=0
            while currentcolsum>colSum[c]:
                diff=currentcolsum-colSum[c]
                maxdiff=min(diff,matrix[r][c])
                matrix[r][c] -=maxdiff
                matrix[r][c+1]+=maxdiff
                currentcolsum -=maxdiff
                r +=1
        return matrix
        