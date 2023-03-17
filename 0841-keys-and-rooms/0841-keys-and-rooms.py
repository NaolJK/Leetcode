class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = deque([0])
        
        visited = set()
        visited.add(0)
        while queue:
            node = queue.popleft()
            for vertex in rooms[node]:
                if vertex not in visited:
                    visited.add(vertex)
                    queue.append(vertex)
                    
        return len(visited) == len(rooms)
            
                