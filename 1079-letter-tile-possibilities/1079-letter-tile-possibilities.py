class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        visited = set()
        ans = set()
        def backtrack(i,path):
            if i > len(tiles):
                return 
            if len(path):
                ans.add(tuple(path[::]))
                
            for j in range(0,len(tiles)):
                if j not in visited:
                    visited.add(j)
                    path.append(tiles[j])
                    backtrack(i+1,path)
                    visited.remove(j)
                    path.pop()
                    
        backtrack(0,[])
        return len(ans)
                
        
            
            
        