class Solution:
    #author :  @PUDDINJK
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        
        #graph container
        graph = defaultdict(list)
        
        #to filter out leaf nodes on the graph
        degree = [0]* (len(roads)+1)
        
        #to count number of rep 
        number_of_rep = [1]*(len(roads)+1)
        
        #builing graph using the ff code
        for v, e in roads:
            graph[e].append(v)
            graph[v].append(e)
            degree[v]+=1
            degree[e]+=1
        
        #since we have to start from the child node we have to start with leaf node meaning nodes with one child
        queue = deque([node for node in range(len(degree)) if degree[node] == 1 and node != 0])
        
        fuel = 0
        
        
        while queue:
            node = queue.popleft()
            
            #calculate the number of coming cars here
            fuel+=ceil(number_of_rep[node]/seats)
           
            for vertex in graph[node]:
                degree[vertex]-=1
                
                #to calculate how many cars or representatives are coming from behind
                number_of_rep[vertex]+=number_of_rep[node]
                
                #if the vertex degree is 1 then there is a rep there if  its more than one we assume we reached the capital
                if degree[vertex] == 1 and vertex != 0:
                    queue.append(vertex)
        
        return fuel
                
            
            