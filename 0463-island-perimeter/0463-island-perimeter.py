class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        self.ans = 0
        
        def bfs(r,c):
            visited.add((r, c))
            queue = deque()
            queue.append((r,c))
            
            while queue:
                row, col = queue.popleft()
                for x,y in directions:
                    new_x , new_y = row+x, col+y
                    out = ((0 > new_x) or (new_x >= rows) or (0 > new_y) or (new_y >= cols))
                    water = (not out and (grid[new_x][new_y] == 0))
                    land = (not out and (grid[new_x][new_y] == 1))
                    if out:
                        self.ans+=1
                    if not out and water:
                        self.ans+=1
                    
                    if not out and land:
                        if (new_x , new_y) not in visited:
                            visited.add((new_x, new_y))
                            queue.append((new_x, new_y))
                            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    bfs(r, c)
                    return self.ans
                    
                    
                    
                
                            
                        
        