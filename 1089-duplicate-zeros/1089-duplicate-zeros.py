class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        idx = 0 
        
        while idx < len(arr):
            if arr[idx] == 0:
                arr.insert(idx,0)
                arr.pop()
                idx+=1
            idx+=1
            
                
                
                
        