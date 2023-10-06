class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        graph = defaultdict(list)
        
        for i in range(len(edges)):
            v, u = edges[i]
            
            graph[v].append((u, succProb[i]))
            graph[u].append((v, succProb[i]))
        
        # print(graph)
        arr = []
        
        heappush(arr, (-1, start_node))
        seen = set()
        
        while arr:
           
            probability, node = heappop(arr)
            
            if node in seen:
                continue
                
            if node == end_node:
                
                return -1*probability
            
            seen.add(node)
            
            for neighbour, weight in graph[node]:
                
                heappush(arr, ((probability*weight), neighbour))
        
        return 0
        
        