class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        maximum = arr.index(max(arr))
        
        i = 0 
        j = len(arr)-1
        
        if len(arr) < 3 or maximum == j or i==maximum:
            return False
        
        while i < maximum:
            if arr[i] >= arr[i+1]:
                return False
            i+=1
        
        while j > maximum:
            if arr[j] >= arr[j-1]:
                return False
            j-=1
        return True
            
                
        