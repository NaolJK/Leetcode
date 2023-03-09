class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        graph = defaultdict(list)
        all_trust = [0]*(n+1)
        source = 0
        for vertex,edge in trust:
            graph[vertex].append(edge)
            all_trust[edge]+=1
            source = vertex
        
        queue = deque()
        visited = set()
        queue.append(source)
        visited.add(source)
        # print(all_trust)
        while queue:
            
            node = queue.popleft()
            if len(graph[node]) == 0 and all_trust[node] == n-1:
                return node
            
            for next_elem in graph[node]:
                if next_elem not in visited:
                    queue.append(next_elem)
                    visited.add(next_elem)
        return -1
        