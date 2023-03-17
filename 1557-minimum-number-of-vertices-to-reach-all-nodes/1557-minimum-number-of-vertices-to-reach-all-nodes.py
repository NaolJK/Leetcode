class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        total_nodes = set(i for i in range(n))
        
        for s, d in edges:
            if d in total_nodes:
                total_nodes.remove(d)
                
        return list(total_nodes)
            
                    