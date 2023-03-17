class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        room = set(i for i in range(len(rooms)))
        queue = deque([0])
        
        visited = set()
        while queue:
            node = queue.popleft()
            if node in room:
                room.remove(node)
            for vertex in rooms[node]:
                if vertex not in visited:
                    visited.add(vertex)
                    queue.append(vertex)
                    
        return len(room) == 0
            
                