class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        #traverse through each row
        for row in range(len(matrix)):
            
            #traverse through each cell to find its top left diagonal element
            for col in range(len(matrix[0])):
                
                #check if we can traverse to back
                if row > 0 and col > 0:
                    
                    #check if the last diagonal is the same as now if not return false
                    if matrix[row][col] != matrix[row-1][col-1]:
                        return False
        
        #return True if all are the same
        return True
                    
                    
                    
                
    
        
        