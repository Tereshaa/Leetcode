class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        rows=len(matrix)
        cols=len(matrix[0])
        min_in_rows = {min(row) for row in matrix}
        
        lucky_numbers = []
        for col in range(len(matrix[0])):
            max_in_col = max(matrix[row][col] for row in range(len(matrix)))
            if max_in_col in min_in_rows:
                lucky_numbers.append(max_in_col)
        
        return lucky_numbers

            
        