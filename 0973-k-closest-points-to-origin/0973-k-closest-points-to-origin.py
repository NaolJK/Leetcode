class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = sorted(points, key= lambda item:math.sqrt((item[0]**2) + (item[1]**2) ))
        return points[:k]
        
            
        
        
        
        
        