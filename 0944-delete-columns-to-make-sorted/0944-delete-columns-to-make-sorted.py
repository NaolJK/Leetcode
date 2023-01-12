class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0 
        
        col_len = len(strs[0])
        row_len = len(strs)
        
        for col in range(col_len):
            for row in range(row_len):
                if row+1 < row_len and strs[row][col] > strs[row+1][col]:
                    count+=1
                    break
        
        return (count)
        
        