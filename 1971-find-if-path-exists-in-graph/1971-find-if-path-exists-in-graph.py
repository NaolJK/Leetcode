class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            
        stack = []
        stack.append(source)
        seen = set([source])
        
        while stack:
            cur = stack.pop()
            
            if cur == destination:
                return True
            
            for next_node in graph[cur]:
                if next_node not in seen:
                    seen.add(next_node)
                    stack.append(next_node)
                    
        return False