class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        
        min_distance = 100000
        idx = -1
        
        for i in range (len(points)):
            if points[i][0] == x or points[i][1] == y:
                res = abs(x - points[i][0]) + abs(y - points[i][1])
                if res < min_distance:
                    min_distance = res 
                    idx = i
        
        return (idx)