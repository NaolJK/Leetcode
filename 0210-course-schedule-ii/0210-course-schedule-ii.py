class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        degree = [0]*numCourses
        visited = set()
        self.cycle = False
        tracker = []
        self.count = 0
        
        #construct the graph
        for courses in prerequisites:
            graph[courses[1]].append(courses[0])
            degree[courses[0]]+=1
        
        queue = deque(i for i in range(numCourses) if degree[i] ==0)
        # print(queue)
        while queue:
            course = queue.popleft()
            self.count+=1
            # print(course)
            tracker.append(course)
            for neighbour in graph[course]:
                # print(neighbour)
                if neighbour in visited:
                    self.cycle = True
                else:
                    degree[neighbour]-=1
                    if degree[neighbour] == 0:
                        queue.append(neighbour)
        if self.cycle:
            return []
        if self.count != numCourses:
            return []
        return tracker
        
            
        