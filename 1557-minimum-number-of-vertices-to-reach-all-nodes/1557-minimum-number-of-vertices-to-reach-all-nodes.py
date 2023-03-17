class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        visited = set()
        
        
        for source, destination in edges:
            graph[source].append(destination)
            graph[destination].append(source)
            visited.add(destination)
            
            
        ans = []
        queue = deque([edges[0][0]])
        seen = set()
        seen.add(edges[0][0])
      
        while queue:
            node = queue.popleft()
            if node not in visited:
                ans.append(node)
                
            for vertex in graph[node]:
                if vertex not in seen:
                    queue.append(vertex)
                    seen.add(vertex)
        return ans
                    