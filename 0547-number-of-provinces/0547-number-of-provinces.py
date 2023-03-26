class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        
        for r in range(len(isConnected)):
            for c in range(len(isConnected[0])):
                if isConnected[r][c] == 1:
                    graph[r+1].append(c+1)
        seen = set()   
        def bfs(source):
            queue = deque([])
            queue.append(source)
            seen.add(source)
            
            while queue:
                node = queue.popleft()
                
                for vertex in graph[node]:
                    if vertex not in seen:
                        queue.append(vertex)
                        seen.add(vertex)
         
        count = 0
        for vertex, edges in graph.items():
            if vertex not in seen:
                count+=1
                bfs(vertex)
                
        return count
            
                        