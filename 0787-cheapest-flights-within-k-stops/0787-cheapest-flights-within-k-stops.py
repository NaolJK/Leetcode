class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        cost = [float('inf')]*(n)
        
        graph = defaultdict(list)
        
        for v1, v2, weight in flights:
    
            graph[v1].append((v2 ,weight))
 
           
        
        pq = []

        
        heappush(pq, (-1,0,src))
        
        cost[src] = 0
        
        while pq:
     
            level, price, node = heappop(pq)
         
                
            for neigh, weight in graph[node]:
                
                d = price + weight
                
                if (level + 1) <= k and d < cost[neigh]: 
                    
                    cost[neigh] = d
                    
                    heappush(pq, (level+1 , d ,neigh))
            
                
                    
        
        if cost[dst] == float('inf'):
            
            return -1
        
        return cost[dst]
    
            
            
        
        