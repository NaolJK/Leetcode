class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        length = len(grid)
        ans = [[0 for i in range(length-2)] for j in range (length-2)]
        
        for i in range(len(ans)):
            for j in range(len(ans)):
                maximum = 0
                for row in range(i,i+3):
                    for col in range (j,j+3):
                        maximum = max(grid[row][col],maximum)
                ans[i][j] = maximum 
                
                
        return ans
        