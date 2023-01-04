class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        transpose = [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0]))]
        
        count = 0
        
        for col in transpose:
            if col in grid:
                total = grid.count(col)
                count+=total
        
        return count