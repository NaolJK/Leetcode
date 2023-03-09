class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        source = 0
        for v,e in edges:
            graph[v].append(e)
            graph[e].append(v)
            source = v
        queue = deque([])
        visited = set()
        queue.append(source)
        visited.add(source)
        
        ans = 0
        
        while queue:
            node = queue.popleft()
            if len(graph[node]) >= 2:
                return node
            for next_elem in graph[node]:
                if next_elem not in visited:
                    queue.append(next_elem)
                    visited.add(next_elem)
            
            
            
        