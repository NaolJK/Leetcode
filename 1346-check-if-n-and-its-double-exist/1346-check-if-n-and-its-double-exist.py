class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        for i,elem in enumerate(arr):
            half = elem/2
            
            if half in arr:
                idx = arr.index(half)
                if idx != i:
                    return True
                
        
        return False
                