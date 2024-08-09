class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def isMagicSquare(x: int, y: int) -> bool:
            nums = [grid[i][j] for i in range(x, x+3) for j in range(y, y+3)]
            
            if sorted(nums) != list(range(1, 10)):
                return False
        
            row_sum = [sum(grid[i][y:y+3]) for i in range(x, x+3)]
            col_sum = [sum(grid[i][j] for i in range(x, x+3)) for j in range(y, y+3)]
            diag_sum1 = sum(grid[x+i][y+i] for i in range(3))
            diag_sum2 = sum(grid[x+i][y+2-i] for i in range(3))
            
            return (
                row_sum[0] == row_sum[1] == row_sum[2] ==
                col_sum[0] == col_sum[1] == col_sum[2] ==
                diag_sum1 == diag_sum2 == 15
            )
        
        rows, cols = len(grid), len(grid[0])
        count = 0
        
        for i in range(rows - 2):
            for j in range(cols - 2):
                if isMagicSquare(i, j):
                    count += 1
        
        return count
        