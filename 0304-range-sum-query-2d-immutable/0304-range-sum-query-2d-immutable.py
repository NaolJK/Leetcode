class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix = [[0 for i in range(len(matrix[0])+1)] for j in range(len(matrix)+1)]
        for r in range(1, len(matrix)+1):
            for c in range(1,len(matrix[0])+1):
                self.prefix[r][c] = matrix[r-1][c-1] + self.prefix[r-1][c] + self.prefix[r][c-1] - self.prefix[r-1][c-1]
        
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        result = self.prefix[row2+1][col2+1] - self.prefix[row1][col2+1] - self.prefix[row2+1][col1] + self.prefix[row1][col1]
        return (result)
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)