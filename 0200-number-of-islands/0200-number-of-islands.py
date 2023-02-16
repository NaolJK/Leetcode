class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        visited = set()
        self.ans = 0
        
        def bfs(r,c):
            visited.add((r,c))
            queue = deque()
            queue.append((r,c))
            
            while queue:
                row, col = queue.popleft()
                for x,y in directions:
                    new_x, new_y = row+x, col+y
                    out = (0 > new_x) or (new_x >= rows) or (0 > new_y) or (new_y >= cols)
                    land = (not out and (grid[new_x][new_y] == "1"))
                    
                    if not out and land and (new_x, new_y) not in visited:
                        visited.add((new_x, new_y))
                        queue.append((new_x, new_y))
            self.ans+=1
        
        for r in range(rows):
            for c in range(cols):
                # print(r,c)
                if (r,c) not in visited and grid[r][c] == "1":
                    bfs(r,c)
        return self.ans
                
        