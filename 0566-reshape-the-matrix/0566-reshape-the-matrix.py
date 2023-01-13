class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        original_row_len = len(mat)
        original_col_len = len(mat[0])
        size = original_row_len * original_col_len
        required = r * c
        
        if required < size or required > size:
            return mat
        reshaped_matrix = [[0 for i in range(c)] for j in range(r)]
        
        for i in range(size):
            original_row = i // original_col_len
            original_col = i % original_col_len
            reshaped_row = i // c
            reshaped_col = i % c
            reshaped_matrix[reshaped_row][reshaped_col] = mat[original_row][original_col]
            
        return reshaped_matrix
                
        
        