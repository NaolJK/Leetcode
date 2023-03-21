class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        minimum = inf
        suffix = [0]*len(grid[0])
        tot = 0

        for i in range(len(grid[0])-1,-1,-1):
            suffix[i] = tot
            tot += grid[0][i]
        
            
        prefix = [0]*len(grid[1])
        prefixSum = 0
        for i in range(len(grid[1])):
            prefix[i] = prefixSum
            prefixSum += grid[1][i] 
        
        for i in range(len(grid[0])):
            minimum = min(minimum, max(prefix[i], suffix[i]))
            
        return minimum
        