class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        graph = defaultdict(list)
        
        for i in range(len(equations)):
            v , e = equations[i]
            value = values[i]
            graph[v].append((e, value))
            graph[e].append((v, 1 / value))
           
            
        
        def bfs(source, target):
            
            arr = deque()
            
            visited = set()
            
            arr.append((1, source))
          
            
            while arr:
                
                val, node = arr.popleft()
                
                if node in visited:
                    
                    continue
                
                visited.add(node)
                
                for vertex, weight in graph[node]:
                    
                    if vertex == target:
                        # print(vertex)
                        return val*weight
                    
                    arr.append((val*weight, vertex))
                    
            return -1
            
        ans = []
        
        for source, target in queries:
            
            res = bfs(source, target)
            
           
            ans.append(res)
            
        return ans
            
            
        
        
        