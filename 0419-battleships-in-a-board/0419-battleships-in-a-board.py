class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        
        seen = set()
        
        def bfs(i, j):
            queue = deque([])
            queue.append((i, j))
            
            seen.add((i, j))
            directions = [(1,0),(-1,0),(0,1),(0,-1)]
            
            
            while queue:
                row, col = queue.pop()
                
                for dx, dy in directions:
                    nr = row + dx
                    nc = col + dy
                    
                    if nr >= 0 and nr < len(board) and nc >= 0 and nc < len(board[0]) and (nr, nc) not in seen and board[nr][nc] == 'X':
                        
                        queue.append((nr, nc))
                        seen.add((nr, nc))
            
        ans = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i, j) not in seen and board[i][j] == 'X':
                    
                    bfs(i, j)
                    ans+=1

        return ans
                        
                        
            
        
        