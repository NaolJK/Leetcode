class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        left, right = 0, len(arr)
        
        while left < right:
            middle = (right+left)//2
            
            if arr[middle-1] < arr[middle] > arr[middle+1]:
                return middle
            
            if arr[middle] < arr[middle+1]:
                left = middle + 1
            else:
                right = middle
                
        return left
            
        