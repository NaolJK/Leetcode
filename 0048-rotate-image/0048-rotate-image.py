class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        top = 0
        down = len(matrix)-1
        right = len(matrix[0])-1
        left = 0
        
        while top <= down:
            ptr1 = right
            ptr2 = left
            while ptr1 >= left and ptr2<=down:
                matrix[top][ptr1], matrix[ptr2][left] = matrix[ptr2][left],matrix[top][ptr1]
                ptr1-=1
                ptr2+=1
                
            
            ptr1 = top+1
            ptr2 = left+1
            
            while ptr1 <= down and ptr2<=right:
                matrix[ptr1][left], matrix[down][ptr2] = matrix[down][ptr2],matrix[ptr1][left]
                ptr1+=1
                ptr2+=1
            

            ptr1 = left+1
            ptr2 = down-1
            
            while ptr2 > top and ptr1 < right:
                matrix[ptr2][right], matrix[down][ptr1] = matrix[down][ptr1],matrix[ptr2][right]
                ptr1+=1
                ptr2-=1
                
            top+=1
            right-=1
            down-=1
            left+=1

                
            
            
                
        