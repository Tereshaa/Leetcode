class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        steps = 1
        res = []
        i = 0
        r, c = rStart, cStart
        
        # Continue until we have covered all cells in the grid
        while len(res) < rows * cols:
            for _ in range(2):  # Each cycle (step) consists of two passes: e.g., right and down
                dr, dc = directions[i]
                for _ in range(steps):
                    # Only add the coordinate if it's within the bounds
                    if 0 <= r < rows and 0 <= c < cols:
                        res.append([r, c])
                    # Move to the next cell in the current direction
                    r += dr
                    c += dc
                # Change direction after finishing a segment of the spiral
                i = (i + 1) % 4
            # Increase step size after completing a full right-down-left-up cycle
            steps += 1
        
        return res

    
 