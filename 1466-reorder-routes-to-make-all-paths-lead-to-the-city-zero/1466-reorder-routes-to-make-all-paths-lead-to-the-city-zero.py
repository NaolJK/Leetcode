class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        
        for v, e in connections:
            graph[v].append(e)
            graph[e].append(v)
            
        queue = deque([0])
        roads = set(tuple(path) for path in connections)
        seen = set()
        seen.add(0)
        
        
        count = 0
        while queue:
            
            node = queue.popleft()
            
            for vertex in graph[node]:
                
                if vertex not in seen:
                    seen.add(vertex)
                    queue.append(vertex)
                
                    if (vertex,node) not in roads:
                        count+=1
                    
        return count
                    
                    
                    
        