class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n = len(image)
        m = len(image[0])
        queue = deque()
        queue.append((sr, sc, image[sr][sc]))
        visited = set()
        visited.add((sr, sc))
        
        while queue:
            row, col, new_color = queue.popleft()
            
            for i, j in [[0,1],[1,0],[-1,0],[0,-1]]:
                new_row, new_col = row + i, col + j
                
                if 0 <= new_row < n and 0<= new_col < m:
                    if image[new_row][new_col] == new_color and (new_row, new_col) not in visited:
                        queue.append((new_row, new_col, new_color))
                        visited.add((new_row, new_col))
        
        for row , col  in visited:
            image[row][col] = color
        
        return image
        
                
        
        