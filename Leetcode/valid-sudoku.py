class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            v = set()
            for col in range(9):
                val = board[row][col]
                if val.isnumeric():
                    if val in v: 
                        return False
                    v.add(val)
                    
        for col in range(9):
            v = set()
            for row in range(9):
                val = board[row][col]
                if val.isnumeric():
                    if val in v: 
                        return False
                    v.add(val)
                    
        for i in range(3):
            for j in range(3):
                v = set()
                for row in range(3):
                    for col in range(3):
                        val = board[row + i*3][col + j*3]
                        if val.isnumeric():
                            if val in v: 
                                return False
                            v.add(val)
                       
        return True