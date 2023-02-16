class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        degrees = [0] * numCourses
        
        for p in prerequisites:
            graph[p[1]].append(p[0])
            degrees[p[0]] += 1
            
        q = deque(n for n in range(numCourses) if degrees[n] == 0)
        count = 0 
        while q:
            course = q.popleft()
            count += 1
            for neighbor in graph[course]:
                degrees[neighbor] -= 1
                if degrees[neighbor] == 0:
                    q.append(neighbor)
        return count == numCourses