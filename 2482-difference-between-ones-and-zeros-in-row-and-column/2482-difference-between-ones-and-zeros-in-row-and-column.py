class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        row_len = len(grid) 
        col_len = len(grid[0])
        row_zeros , col_zeros = [0]*row_len, [0]*col_len

        for row in range(row_len):
            for col in range(col_len):
                if grid[row][col] == 0 :
                    row_zeros[row] +=1
                    col_zeros[col] +=1

        for row in range(row_len):
            for col in range(col_len):
                zeros = row_zeros[row] + col_zeros[col]
                ones = (row_len - row_zeros[row]) + (col_len-col_zeros[col])
                grid[row][col] = ones - zeros
                
        return grid
        