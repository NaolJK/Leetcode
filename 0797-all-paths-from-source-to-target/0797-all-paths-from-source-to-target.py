class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        queue = deque([(0,[0])])
        ans =[]
        length = len(graph)
        
        while queue:
            node,path = queue.popleft()
            
            if node == length-1:
                ans.append(path)
            
            for vertex in graph[node]:
                
                queue.append((vertex, path+[vertex]))
                
        return ans 